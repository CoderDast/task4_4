class ContactList(list):
    def __init__(self, *args):
        self.contacts = args

    def search_by_name(self, name):
        """
        Показывает индекс контакта
        """
        if name in self.contacts:
            return self.contacts.index(name)
        else:
            return "This contact doesn't exist!!!"


all_contacts = ContactList("Super", "Mega", "Pushka", "Perfect", "Cool", "Impossible","Unbelieveble")
print(all_contacts.search_by_name("Super"))
print(all_contacts.search_by_name("Pushka"))
print(all_contacts.search_by_name("Cool"))