from wild_cat.category import Category
from wild_cat.document import Document
from wild_cat.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic:Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        for c in self.categories:
            if c.id == category_id:
                c.name = new_name


    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for t in self.topics:
            if t.id == topic_id:
                t.topic = new_topic
                t.storage_folder = new_storage_folder
                break

    def edit_document(self, document_id: int, new_file_name: str):
        for d in self.documents:
            if d.id == document_id:
                d.file_name = new_file_name

    def delete_category(self, category_id):
        for c in self.categories:
            if c.id == category_id:
                self.categories.remove(c)
                break

    def delete_topic(self, topic_id):
        for t in self.topics:
            if t.id == topic_id:
                self.topics.remove(t)
                break

    def delete_document(self, document_id):
        for d in self.documents:
            if d.id == document_id:
                self.documents.remove(d)
                break

    def get_document(self, document_id):
        for d in self.documents:
            if d.id == document_id:
                return repr(d)

    def __repr__(self):
        docs = '\n'.join(c.__repr__() for c in self.documents)
        return docs


# c1 = Category(1, 'work')
# t1 = Topic(1, 'daily tasks', 'C:\\work_documents')
# d1 = Document(1, 1, 1, 'finilize animals')
# d1.add_tag('urgent')
# d1.add_tag('work')
# storage = Storage()
# storage.add_category(c1)
# storage.add_topic(t1)
# storage.add_document(d1)
# print(c1)
# print(t1)
# print(storage.get_document(1))
# print(storage)