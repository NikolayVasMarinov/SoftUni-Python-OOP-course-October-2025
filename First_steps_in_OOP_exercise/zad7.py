class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name: str, language: str, skills_earned: int) -> str:
        if language != self.language:
            return f"{self.name} does not know {language}"

        self.skills += skills_earned
        return f"{self.name} watched {course_name}"

    def change_language(self, new_language: str, skills_needed: int) -> str:
        if self.skills < skills_needed:
            return f"{self.name} needs {skills_needed - self.skills} more skills"

        if self.language == new_language:
            return f"{self.name} already knows {new_language}"

        result = f"{self.name} switched from {self.language} to {new_language}"
        self.language = new_language
        return result