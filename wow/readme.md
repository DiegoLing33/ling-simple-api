# Prestij.xyz API

- Получение списка гильдейцев со всей экстра информацией
    ```
    GET http://server.prestij.xyz/characters/list
    ```
    Имеются параметры offset и limit для переключения "по страницам".
    

- Получение всей информации о гильдейце
  ```
  GET http://server.prestij.xyz/characters/имя_персонажа
  ```
  **Внимание!** Не рекомендуется использовтаь два метода `/charcter/list` и `/character/имя` вместе. Лучшее решение будет - скачать всю информацию, используя
  первый метод (`/characters/list`) и оперерировать ею. Как это сделано на http://prestij.xyz
  
- Получение информации о гильдии
    ```
    GET http://server.prestij.xyz/guild
    ```
  
 - Получение изображения персонажа
    ```
   http://server.prestij.xyz/static/characters/{имя с маленькой буквы}_main.png
   ```
   
 - Получение "аватарки" пресонажа
     ```
   http://server.prestij.xyz/static/characters/{имя с маленькой буквы}_avatar.jpg
   ```
 
 - Получение изображения предмета эпикировки
     ```
   http://server.prestij.xyz/static/items/{image_id}.jpg
   ```
   image_id можно получить в объекте экипировки
 