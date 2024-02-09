
class Doctor:
    doctor_professions = {
                            "neurologist": [
                                {"name": "Dr. Alice", "contact": "1234567890"},
                                {"name": "Dr. Bob", "contact": "9876543210"},
                                {"name": "Dr. Chris", "contact": "1234567890"},
                                {"name": "Dr. David", "contact": "9876543210"},
                                {"name": "Dr. Eric", "contact": "1234567890"}
                            ],
                            "psychiatrist": [
                                {"name": "Dr. Sita", "contact": "9876543210"},
                                {"name": "Dr. Mary", "contact": "9876543210"},
                                {"name": "Dr. John", "contact": "9876543210"},
                                {"name": "Dr. Emily", "contact": "9876543210"},
                                {"name": "Dr. Richard", "contact": "9876543210"}
                            ],
                            "cardiologist": [
                                {"name": "Dr. Deals", "contact": "9876543210"},
                                {"name": "Dr. Smith", "contact": "9876543210"},
                                {"name": "Dr. Lisa", "contact": "9876543210"},
                                {"name": "Dr. James", "contact": "9876543210"},
                                {"name": "Dr. Grace", "contact": "9876543210"}
                            ],
                            "dermatologist": [
                                {"name": "Dr. Hari", "contact": "9876543210"},
                                {"name": "Dr. Jane", "contact": "9876543210"},
                                {"name": "Dr. Michael", "contact": "9876543210"},
                                {"name": "Dr. Lily", "contact": "9876543210"},
                                {"name": "Dr. Brian", "contact": "9876543210"}
                            ],
                            "orthopedic_surgeon": [
                                {"name": "Dr. Alex", "contact": "9876543210"},
                                {"name": "Dr. Emma", "contact": "9876543210"},
                                {"name": "Dr. Kevin", "contact": "9876543210"},
                                {"name": "Dr. Sophia", "contact": "9876543210"},
                                {"name": "Dr. Robert", "contact": "9876543210"}
                            ],
                            "ophthalmologist": [
                                {"name": "Dr. Mark", "contact": "9876543210"},
                                {"name": "Dr. Jessica", "contact": "9876543210"},
                                {"name": "Dr. Matthew", "contact": "9876543210"},
                                {"name": "Dr. Ava", "contact": "9876543210"},
                                {"name": "Dr. Benjamin", "contact": "9876543210"}
                            ],
                            "dentist": [
                                {"name": "Dr. Chloe", "contact": "9876543210"},
                                {"name": "Dr. Ethan", "contact": "9876543210"},
                                {"name": "Dr. Lauren", "contact": "9876543210"},
                                {"name": "Dr. Jackson", "contact": "9876543210"},
                                {"name": "Dr. Zoey", "contact": "9876543210"}
                            ],
                            "pediatrician": [
                                {"name": "Dr. Oliver", "contact": "9876543210"},
                                {"name": "Dr. Lily", "contact": "9876543210"},
                                {"name": "Dr. Noah", "contact": "9876543210"},
                                {"name": "Dr. Isabella", "contact": "9876543210"},
                                {"name": "Dr. William", "contact": "9876543210"}
                            ],
                            "gynecologist": [
                                {"name": "Dr. Mia", "contact": "9876543210"},
                                {"name": "Dr. Samuel", "contact": "9876543210"},
                                {"name": "Dr. Sophia", "contact": "9876543210"},
                                {"name": "Dr. Aiden", "contact": "9876543210"},
                                {"name": "Dr. Emily", "contact": "9876543210"}
                            ],
                            "urologist": [
                                {"name": "Dr. Ethan", "contact": "9876543210"},
                                {"name": "Dr. Ava", "contact": "9876543210"},
                                {"name": "Dr. Logan", "contact": "9876543210"},
                                {"name": "Dr. Mia", "contact": "9876543210"},
                                {"name": "Dr. William", "contact": "9876543210"}
                            ],
                            "otolaryngologist": [
                                {"name": "Dr. Zoey", "contact": "9876543210"},
                                {"name": "Dr. Benjamin", "contact": "9876543210"},
                                {"name": "Dr. Chloe", "contact": "9876543210"},
                                {"name": "Dr. Jackson", "contact": "9876543210"},
                                {"name": "Dr. Ava", "contact": "9876543210"}
                            ],
                            "gastroenterologist": [
                                {"name": "Dr. William", "contact": "9876543210"},
                                {"name": "Dr. Emily", "contact": "9876543210"},
                                {"name": "Dr. Samuel", "contact": "9876543210"},
                                {"name": "Dr. Lily", "contact": "9876543210"},
                                {"name": "Dr. Aiden", "contact": "9876543210"}
                            ],
                            "oncologist": [
                                {"name": "Dr. Mia", "contact": "9876543210"},
                                {"name": "Dr. Ethan", "contact": "9876543210"},
                                {"name": "Dr. Logan", "contact": "9876543210"},
                                {"name": "Dr. Sophia", "contact": "9876543210"},
                                {"name": "Dr. Benjamin", "contact": "9876543210"}
                            ],
                            "radiologist": [
                                {"name": "Dr. Chloe", "contact": "9876543210"},
                                {"name": "Dr. Jackson", "contact": "9876543210"},
                                {"name": "Dr. Zoey", "contact": "9876543210"},
                                {"name": "Dr. William", "contact": "9876543210"},
                                {"name": "Dr. Ava", "contact": "9876543210"}
                            ],
                            "emergency_physician": [
                                {"name": "Dr. Aiden", "contact": "9876543210"},
                                {"name": "Dr. Mia", "contact": "9876543210"},
                                {"name": "Dr. Logan", "contact": "9876543210"},
                                {"name": "Dr. Emily", "contact": "9876543210"},
                                {"name": "Dr. Samuel", "contact": "9876543210"}
                            ],
                            "rheumatologist": [
                                {"name": "Dr. Lily", "contact": "9876543210"},
                                {"name": "Dr. Benjamin", "contact": "9876543210"},
                                {"name": "Dr. Chloe", "contact": "9876543210"},
                                {"name": "Dr. Jackson", "contact": "9876543210"},
                                {"name": "Dr. Zoey", "contact": "9876543210"}
                            ],
                            "endocrinologist": [
                                {"name": "Dr. William", "contact": "9876543210"},
                                {"name": "Dr. Ava", "contact": "9876543210"},
                                {"name": "Dr. Aiden", "contact": "9876543210"},
                                {"name": "Dr. Emily", "contact": "9876543210"},
                                {"name": "Dr. Samuel", "contact": "9876543210"}
                            ],
                            "pulmonologist": [
                                {"name": "Dr. Mia", "contact": "9876543210"},
                                {"name": "Dr. Ethan", "contact": "9876543210"},
                                {"name": "Dr. Logan", "contact": "9876543210"},
                                {"name": "Dr. Sophia", "contact": "9876543210"},
                                {"name": "Dr. Benjamin", "contact": "9876543210"}
                            ],
                            "nephrologist": [
                                {"name": "Dr. Chloe", "contact": "9876543210"},
                                {"name": "Dr. Jackson", "contact": "9876543210"},
                                {"name": "Dr. Zoey", "contact": "9876543210"},
                                {"name": "Dr. William", "contact": "9876543210"},
                                {"name": "Dr. Ava", "contact": "9876543210"}
                            ],
                            "anesthesiologist": [
                                {"name": "Dr. Aiden", "contact": "9876543210"},
                                {"name": "Dr. Mia", "contact": "9876543210"},
                                {"name": "Dr. Logan", "contact": "9876543210"},
                                {"name": "Dr. Emily", "contact": "9876543210"},
                                {"name": "Dr. Samuel", "contact": "9876543210"}
                            ],
                            "gastrointestinal_surgeon": [
                                {"name": "Dr. Lily", "contact": "9876543210"},
                                {"name": "Dr. Benjamin", "contact": "9876543210"},
                                {"name": "Dr. Chloe", "contact": "9876543210"},
                                {"name": "Dr. Jackson", "contact": "9876543210"},
                                {"name": "Dr. Zoey", "contact": "9876543210"}
                            ],
                            }


    @classmethod
    def display_profession(cls, profession_key):
        # Handle invalid key
        if profession_key not in cls.doctor_professions:
            return "Invalid profession. Please choose from available options."

        # Retrieve the list of doctors for the given profession
        doctors = cls.doctor_professions[profession_key]

        # Build the output by iterating through the list of doctors
        output = f"\n**Doctors in {profession_key} profession:**"
        for doctor in doctors:
            output += f"\n - Name: {doctor['name']}\n   Contact: {doctor['contact']}"

        return output

