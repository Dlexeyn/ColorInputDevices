import colorgram
import sys
import xml.etree.ElementTree as ET


def save_file(text):
    # Создание корневого элемента
    root = ET.Element("Root")

    # Создание и добавление дочерних элементов
    description = ET.SubElement(root, "Description")
    description.text = "ckPannel:\nFor custom-made RGB partition"

    light_effect = ET.SubElement(root, "LightEffect")
    light_effect.text = "1"

    breathe_speed = ET.SubElement(root, "BreatheSpeed")
    breathe_speed.text = "2"

    color_picture = ET.SubElement(root, "ColorPicture")
    color_picture.text = ("A449A3,0000FF,0000FF,0000FF,0000FF,0000FF,0000FF,0000FF,0000FF,0000FF,0000FF,0000FF,0000FF,"
                          "A449A3,A449A3,000000,000000,000000")

    # Создание дерева XML
    tree = ET.ElementTree(root)

    # Запись в файл с кодировкой UTF-16
    with open("output.ckPannel", "wb") as file:
        tree.write(file, encoding="utf-16", xml_declaration=True)


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


def main():
    wall = sys.argv[1] if len(sys.argv) > 1 else "No Path to Image"

    print(f"Wallpaper: {wall}")
    colors = colorgram.extract(wall, 7)

    colors_hex = [rgb_to_hex(color) for color in colors]

    for i, color in enumerate(colors):
        print(f"color {i + 1} - {color.rgb}")


if __name__ == "__main__":
    main()
