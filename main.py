# Getting The GWA
from pyscript import document

def getting_gwa(e):
    name = document.getElementById("inputText").value
    math_grade = float(document.getElementById("inputMathGrade").value)
    science_grade = float(document.getElementById("inputScienceGrade").value)
    english_grade = float(document.getElementById("inputEnglishGrade").value)
    social_studies_grade = float(document.getElementById("inputSocialStudiesGrade").value)
    music_grade = float(document.getElementById("inputMusicGrade").value)
    pe_grade = float(document.getElementById("inputPEGrade").value)

    # 💯 Your original formula
    gwa = (math_grade + science_grade + english_grade + social_studies_grade + music_grade + pe_grade) / 6

    # Show result on page
    document.getElementById("result").innerText = f"{name}'s GWA is {gwa}"