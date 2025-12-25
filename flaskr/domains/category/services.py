from typing import List,Any,Dict

from flask import abort
from sqlalchemy.sql.functions import user

from flaskr.domains.category.models import Category
from flaskr.domains.category.repositories import CategoryRepository

class CategoryService:
    repository=CategoryRepository()

    def get_by_id(self, item_id: int) -> Any | None:

       category = self.repository.get_by_id(item_id=item_id)

       if category is None:
           abort(404,description="Category not found")

       response =category.serialize
       return response

    def list_categories(self) -> List:
        categories = self.repository.get_all()

        all_categories = []
        for category in categories:
            all_categories.append(category.serialize)

        return all_categories

    def create_new_category(self,
                            name:str)-> Dict | None:
        new_category=self.repository.add(Category(name=name))

        category_id = new_category.serialize.get('id')
        if category_id :
            return self.get_by_id(category_id)

    def update_category(self,
                        category_id: int,
                        data:Dict)-> Dict | None:
        self.get_by_id(item_id=category_id)
        response=self.repository.update(item_id=category_id,data=data)
        if response :
            return self.get_by_id(item_id=category_id)


    def delete_category(self,item_id:int )->bool:
        self.get_by_id(item_id=item_id)
        return self.repository.delete(item_id=item_id)









