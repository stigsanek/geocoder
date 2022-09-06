# py-csv-geocoder

Determination of geocoordinates by address or vice versa from a csv file

## Configuring data

In the project directory create file `.env` and set data:

```
API_KEY="your Yandex token"

# IS_REVERSE=1 - geocoding by address
# IS_REVERSE=0 - geocoding by coordinates
IS_REVERSE=0
```

* For direct geocoding, add to `input.csv` data in the format: `id;address`.

```
1;Самарская область, п. Пахарь, ул. Набережная, 18
2;Московская область, с. Раменки, ул. 30 лет Победы, 2
3;Камчатский край, г. Петропавловск-Камчатский, Океанская улица, 102
...
```

* For reverse geocoding, add data to the `input.csv` in the format: `id;latitude;longitude;address`.

```
1;50.430818;53.006853;Россия;Приволжский федеральный округ;Самарская область;Волжский район;поселок Пахарь;Набережная улица;18
2;39.157204;55.173149;Россия;Центральный федеральный округ;Московская область;городской округ Егорьевск;село Раменки;улица 30 лет Победы;2
3;158.683972;52.981172;Россия;Дальневосточный федеральный округ;Камчатский край;городской округ Петропавловск-Камчатский;Петропавловск-Камчатский;Океанская улица;102
...
```

## Application launch

In the project directory do:
* `python -m venv venv && cd venv\Scripts && activate && cd ..\..\`
* `pip install -r requirements.txt`
* `python -m geocoder`
