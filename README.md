# py-csv-geocoder
Determination of geocoordinates by address or vice versa from a csv file

## Configuring data

* Set your api key Yandex and geocoding order in `start.py`:

```
APY_KEY = 'set_api_key'
run_geocoder(APY_KEY, is_reverse=True) #is_reverse - geocoding order parameter
```

* For direct geocoding, add to `input.csv` data in the format: `id;address`.

```
1;Самарская область, п. Пахарь, ул. Набережная, 18
2;Московская область, с. Раменки, ул. 30 лет Победы, 2
3;Камчатский край, г. Петропавловск-Камчатский, Океанская улица, 102
...
```

* For reverse geocoding, add data to the `input.csv` in the format: `id;latitude;longitude`.

```
1;51.086416;52.474101
2;51.09315;52.476077
3;51.278689;52.577568
...
```

## Application launch

* Install [Python](https://www.python.org/)
* Run `pip install requests`
* In the project directory run `python start.py`
