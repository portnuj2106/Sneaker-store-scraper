import re


def get_name(page):
    name = page.find('h1', class_='mt-2 mb-1').text
    return name


def get_price(page):
    try:
        match = re.search(r'\d+\.\d+', page.find('span', class_='h3').text)
        with_discount = float(match.group())
        price_container = page.find('span', class_='h3')
        price = price_container.find('span', class_='strike').text
    except AttributeError:
        match = re.search(r'\d+\.\d+', page.find('span', class_='h3').text)
        if match:
            price = float(match.group())
        else:
            price = "No price found"
        with_discount = "No discount"
    return price, with_discount


def get_description(page):
    try:
        content_description = page.find('div', id='content-description')
        description = content_description.find('p').text
    except AttributeError:
        description = "No description"
    return description


def get_details(page):
    details_body = page.find('div', id='content-details')
    details = details_body.find('tbody')
    details_list = details.find_all('tr')
    try:
        style = details_list[0].find('td').text.strip()
    except AttributeError or IndexError:
        style = "No style"

    try:
        colorway = details_list[1].find('td').text.strip()
    except AttributeError or IndexError:
        colorway = "No colorway"

    try:
        gender = details_list[2].find('td').text.strip()
    except AttributeError or IndexError:
        gender = "No gender"

    try:
        material = details_list[3].find('td').text.strip()
    except AttributeError or IndexError:
        material = "No material"

    try:
        manufacturer = details_list[4].find('td').text.strip()
    except AttributeError or IndexError:
        manufacturer = "No manufacturer"

    try:
        series = details_list[5].find('td').text.strip()
    except AttributeError or IndexError:
        series = "No series"

    try:
        purpose = details_list[6].find('td').text.strip()
    except AttributeError or IndexError:
        purpose = "No purpose"

    return style, colorway, gender, material, manufacturer, series, purpose
