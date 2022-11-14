import pytest as pytest

from nickname_parser import get_file_content, parse_nickname, save_nicknames, main


def test_get_file_content_happy_path():
    res = get_file_content('examples/example_1.txt')

    assert res


def test_get_file_content_wrong_path():
    with pytest.raises(FileNotFoundError):
        get_file_content('wrong_file.txt')


def test_parse_nickname_happy_path():
    text_str = 'Taiwanese 🇹🇼 @supcaitlin\nCambodian 🇰🇭 and Vietnamese 🇻🇳 @rosettehing @tEst.test @Test12 @tesT_3'

    res = parse_nickname(text_str)

    assert res == ['@supcaitlin', '@rosettehing', '@tEst.test', '@Test12', '@tesT_3']


def test_parse_nickname_no_nicknames():
    text_str = 'Taiwanese 🇹🇼 supcaitlin\nCambodian 🇰🇭 and Vietnamese 🇻🇳 rosettehing tEst.test Test12 tesT_3'

    res = parse_nickname(text_str)

    assert res == []


def test_save_nicknames_happy_path():
    nickname_list = ['@supcaitlin', '@rosettehing', '@tEst.test', '@Test12', '@tesT_3']
    output_file_address = 'output/output_example_1.txt'

    save_nicknames(nickname_list, output_file_address)

    file_content = get_file_content('output/output_example_1.txt')
    res = parse_nickname(file_content)

    assert res == nickname_list


def test_save_nicknames_invalid_path():
    with pytest.raises(FileNotFoundError):
        save_nicknames([], 'wrong_folder/wrong_file.txt')


def test_main_smoke():
    res = main('examples/example_1.txt', 'output/test_1.txt')

    assert res is None
