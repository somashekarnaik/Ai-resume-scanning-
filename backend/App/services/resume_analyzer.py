from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .skill_extractor import extract_skills


def calculate_similarity(resume_text, job_description):
    if not resume_text.strip() or not job_description.strip():
        return 0

    documents = [resume_text, job_description]
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(documents)
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(similarity * 100, 2)


def analyze_resume(resume_text, job_description):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched_skills = [skill for skill in job_skills if skill in resume_skills]
    missing_skills = [skill for skill in job_skills if skill not in resume_skills]

    if job_skills:
        skill_score = (len(matched_skills) / len(job_skills)) * 100
    else:
        skill_score = 0

    similarity_score = calculate_similarity(resume_text, job_description)
    overall_score = (skill_score * 0.6) + (similarity_score * 0.4)

    recommendations = [
        f"Consider adding {skill} if you have experience with it."
        for skill in missing_skills
    ]

    if not recommendations:
        recommendations.append("Your resume matches the required skills well.")

    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "skill_score": round(skill_score, 2),
        "similarity_score": similarity_score,
        "overall_score": round(overall_score, 2),
        "recommendations": recommendations,
    }