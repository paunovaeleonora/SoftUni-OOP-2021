import math

_PAGE_PHOTOS: int = 4
_SUCCESS: str = 'photo added successfully on page'
_FAILED: str = 'No more free slots'
_DASHES: str = f"{11 * '-'}\n"


class PhotoAlbum:
    PAGE_PHOTOS = _PAGE_PHOTOS
    SUCCESS = _SUCCESS
    FAILED = _FAILED
    DASHES = _DASHES

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for p in range(pages)]
        self.page_index = 0

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages: int = math.ceil(photos_count / cls.PAGE_PHOTOS)
        return cls(pages)

    def is_space(self)-> bool:
        return self.page_index < self.pages and len(self.photos[self.page_index]) < self.PAGE_PHOTOS

    def new_page(self) -> int:
        if len(self.photos[self.page_index]) == self.PAGE_PHOTOS:
            self.page_index += 1
        return self.page_index

    def add_photo(self, label):
        if not self.is_space():
            return self.FAILED

        self.photos[self.page_index].append(str(label))

        added_photo = f'{label} {self.SUCCESS} {self.page_index + 1} slot {len(self.photos[self.page_index])}'
        self.new_page()
        return added_photo

    def display(self):
        display = self.DASHES
        for _ in self.photos:
            if _:
                display += ''.join('[] ' for i in range(len(_))).strip()
            display += f'\n{self.DASHES}'
        return display


album = PhotoAlbum(2)
print(album.add_photo('baby'))
print(album.add_photo('first grade'))
print(album.add_photo('eight grade'))
print(album.add_photo('party with friends'))
print(album.photos)
print(album.add_photo('prom'))
print(album.add_photo('wedding'))
print(album.display())