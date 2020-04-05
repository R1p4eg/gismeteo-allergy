#Описание:
Сенсор прогназы пыльцы берёзы на 10 дней по данным Gismeteo.
Собирает данные о прогнозе пыльцы, а так же день недели и число и складывает это в атрибуты сенсора

#Установка:
Устанавливается через HACS или копированием директории `custom_components/gismeteo-allergy` в стандартную директорию компонентов HA

#Настройка:

##Параметр city:
Для получения прогноза по конкретному городу необходимо перейти на сайт https://www.gismeteo.ru/, найти свой город в поиске и скопировать из адресной строки браузера идентификатор вашего города, который идет после `weather`. 
К примеру, для Москвы URL имеет вид:  `https://www.gismeteo.ru/weather-moscow-4368/10-days/`, соответственно идентификатор будет равен `moscow-4368`

Этот идентификатор прописывается в поле `city`

##Параметр scan_interval
Опциональный, по умолчанию - апдейт раз в 12 часов

#Примеры:
Минимальный пример, в значении этого сенсора будет количество пыльцы на сегодняшний день, в атрибутах все остальные дни
```yaml
- platform: gismeteo_allergy
  name: Береза Москва
  city:
    moscow-4368
  scan_interval: '02:00:00'
    
- platform: gismeteo_allergy
  name: Береза Питер
  city:
    sankt-peterburg-4079
```

Пример полного конфига сенсоров для Москвы на 10 дней с динамически изменяемой иконкой (в зависимости от концентрации пыльцы) и friendly_name (содержит в себе день недели и число).
```yaml
- platform: gismeteo_allergy
  name: Береза Москва
  city:
    moscow-4368
  scan_interval: '02:00:00'
    
  
- platform: template
  sensors:
    moscow_today:
      friendly_name_template: "{{ state_attr('sensor.bereza_moskva', 'day_0')['day'] }}"
      value_template: "{{ state_attr('sensor.bereza_moskva', 'day_0')['value'] }}"
      icon_template: >
        {% if state_attr('sensor.bereza_moskva', 'day_0')['value']  <= 10 %}
            mdi:emoticon-happy-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_0')['value']  <= 50 %}
           mdi:emoticon-neutral-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_0')['value']  <= 500 %}
           mdi:emoticon-sad-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_0')['value']  > 500 %}
           mdi:emoticon-dead-outline
        {% endif %}

    moscow_tommorrow:
      friendly_name_template: "{{ state_attr('sensor.bereza_moskva', 'day_1')['day'] }}"
      value_template: "{{ state_attr('sensor.bereza_moskva', 'day_1')['value'] }}"
      icon_template: >
        {% if state_attr('sensor.bereza_moskva', 'day_1')['value']  <= 10 %}
            mdi:emoticon-happy-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_1')['value']  <= 50 %}
           mdi:emoticon-neutral-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_1')['value']  <= 500 %}
           mdi:emoticon-sad-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_1')['value']  > 500 %}
           mdi:emoticon-dead-outline
        {% endif %}
      
    moscow_day_3:
      friendly_name_template: "{{ state_attr('sensor.bereza_moskva', 'day_2')['day'] }}"
      value_template: "{{ state_attr('sensor.bereza_moskva', 'day_2')['value'] }}"
      icon_template: >
        {% if state_attr('sensor.bereza_moskva', 'day_2')['value']  <= 10 %}
            mdi:emoticon-happy-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_2')['value']  <= 50 %}
           mdi:emoticon-neutral-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_2')['value']  <= 500 %}
           mdi:emoticon-sad-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_2')['value']  > 500 %}
           mdi:emoticon-dead-outline
        {% endif %}

    moscow_day_4:
      friendly_name_template: "{{ state_attr('sensor.bereza_moskva', 'day_3')['day'] }}"
      value_template: "{{ state_attr('sensor.bereza_moskva', 'day_3')['value'] }}"
      icon_template: >
        {% if state_attr('sensor.bereza_moskva', 'day_3')['value']  <= 10 %}
            mdi:emoticon-happy-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_3')['value']  <= 50 %}
           mdi:emoticon-neutral-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_3')['value']  <= 500 %}
           mdi:emoticon-sad-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_3')['value']  > 500 %}
           mdi:emoticon-dead-outline
        {% endif %}

    moscow_day_5:
      friendly_name_template: "{{ state_attr('sensor.bereza_moskva', 'day_4')['day'] }}"
      value_template: "{{ state_attr('sensor.bereza_moskva', 'day_4')['value'] }}"
      icon_template: >
        {% if state_attr('sensor.bereza_moskva', 'day_4')['value']  <= 10 %}
            mdi:emoticon-happy-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_4')['value']  <= 50 %}
           mdi:emoticon-neutral-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_4')['value']  <= 500 %}
           mdi:emoticon-sad-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_4')['value']  > 500 %}
           mdi:emoticon-dead-outline
        {% endif %}

    moscow_day_6:
      friendly_name_template: "{{ state_attr('sensor.bereza_moskva', 'day_5')['day'] }}"
      value_template: "{{ state_attr('sensor.bereza_moskva', 'day_5')['value'] }}"
      icon_template: >
        {% if state_attr('sensor.bereza_moskva', 'day_5')['value']  <= 10 %}
            mdi:emoticon-happy-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_5')['value']  <= 50 %}
           mdi:emoticon-neutral-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_5')['value']  <= 500 %}
           mdi:emoticon-sad-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_5')['value']  > 500 %}
           mdi:emoticon-dead-outline
        {% endif %}
      
    moscow_day_7:
      friendly_name_template: "{{ state_attr('sensor.bereza_moskva', 'day_6')['day'] }}"
      value_template: "{{ state_attr('sensor.bereza_moskva', 'day_6')['value'] }}"
      icon_template: >
        {% if state_attr('sensor.bereza_moskva', 'day_6')['value']  <= 10 %}
            mdi:emoticon-happy-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_6')['value']  <= 50 %}
           mdi:emoticon-neutral-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_6')['value']  <= 500 %}
           mdi:emoticon-sad-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_6')['value']  > 500 %}
           mdi:emoticon-dead-outline
        {% endif %}

    moscow_day_8:
      friendly_name_template: "{{ state_attr('sensor.bereza_moskva', 'day_7')['day'] }}"
      value_template: "{{ state_attr('sensor.bereza_moskva', 'day_7')['value'] }}"
      icon_template: >
        {% if state_attr('sensor.bereza_moskva', 'day_7')['value']  <= 10 %}
            mdi:emoticon-happy-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_7')['value']  <= 50 %}
           mdi:emoticon-neutral-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_7')['value']  <= 500 %}
           mdi:emoticon-sad-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_7')['value']  > 500 %}
           mdi:emoticon-dead-outline
        {% endif %}
      
    moscow_day_9:
      friendly_name_template: "{{ state_attr('sensor.bereza_moskva', 'day_8')['day'] }}"
      value_template: "{{ state_attr('sensor.bereza_moskva', 'day_8')['value'] }}"
      icon_template: >
        {% if state_attr('sensor.bereza_moskva', 'day_8')['value']  <= 10 %}
            mdi:emoticon-happy-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_8')['value']  <= 50 %}
           mdi:emoticon-neutral-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_8')['value']  <= 500 %}
           mdi:emoticon-sad-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_8')['value']  > 500 %}
           mdi:emoticon-dead-outline
        {% endif %}
      
    moscow_day_10:
      friendly_name_template: "{{ state_attr('sensor.bereza_moskva', 'day_9')['day'] }}"
      value_template: "{{ state_attr('sensor.bereza_moskva', 'day_9')['value'] }}"
      icon_template: >
        {% if state_attr('sensor.bereza_moskva', 'day_9')['value']  <= 10 %}
            mdi:emoticon-happy-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_9')['value']  <= 50 %}
           mdi:emoticon-neutral-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_9')['value']  <= 500 %}
           mdi:emoticon-sad-outline
        {% elif state_attr('sensor.bereza_moskva', 'day_9')['value']  > 500 %}
           mdi:emoticon-dead-outline
        {% endif %}
```