import re


SKILLS = [

    "python",
    "java",
    "c++",
    "javascript",
    "typescript",

    "html",
    "css",

    "react",
    "node.js",

    "fastapi",
    "django",
    "flask",

    "sql",
    "mysql",
    "postgresql",
    "mongodb",

    "machine learning",
    "deep learning",

    "artificial intelligence",

    "natural language processing",
    "nlp",

    "tensorflow",
    "pytorch",

    "scikit-learn",

    "pandas",
    "numpy",

    "git",
    "github",

    "docker",

    "aws",
    "azure",

    "data analysis",

    "power bi",

    "excel",

    "software testing",
    "rest api",
    "financial analysis",
    "financial modeling",
    "forecasting",
    "budgeting",
    "accounting",
    "financial statements"

]


def extract_skills(text):

    text = text.lower()

    found = []


    for skill in SKILLS:

        pattern = (
            r"(?<!\w)"
            + re.escape(skill)
            + r"(?!\w)"
        )


        if re.search(
            pattern,
            text
        ):

            found.append(
                skill
            )


    return sorted(
        set(found)
    )