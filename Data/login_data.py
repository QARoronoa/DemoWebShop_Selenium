from faker import Faker

faker = Faker(locale='FR_fr')
class login:

    @staticmethod
    def fill_register_form():
        password = faker.password()
        return {
            "firstName" : faker.first_name(),
            "lastName" : faker.last_name(),
            "email" : faker.email(),
            "password" : password,
            "confirmPassword" : password
        }

    @staticmethod
    def fill_register_form_avec_credentials_existant():
        password = faker.password()
        return {
            "firstName" : faker.first_name(),
            "lastName" : faker.last_name(),
            "email" : 'mdenis@example.com',
            "password" : '^5W5L9z2q3',
            "confirmPassword" : '^5W5L9z2q3'
        }



