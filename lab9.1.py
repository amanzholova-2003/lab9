def get_skills(resume):
    return resume.get('skills')
def print_resume(resume):
    print("Name: " + resume.get('name'))
    print("Age: " + resume.get('age'))
    print("Education: " + resume.get('education'))
    print("Skills: " + "".join(resume.get('skills')))

resume = {'name':'Zeinep','age': '19','education':'Satbayev university', 'skills':'programming smart strong'}
print(get_skills(resume))
print()
print_resume(resume)