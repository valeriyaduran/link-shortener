from unittest import mock

import pytest

from src.app.link_shortener import prepare_shortened_link, get_shortened_link_id
from src.config import dev_domain


class TestPrepareShortenedLink:
    @mock.patch("src.app.link_shortener.get_generated_value")
    @pytest.mark.parametrize("origin_link, expected_result",
                             [("https://test.com/123123", f"{dev_domain}A1B2c3")])
    def test_shorten_link_success(self, mocked_generated, origin_link, expected_result):
        mocked_generated.return_value = 'A1B2c3'
        assert prepare_shortened_link() == expected_result


class TestGetLinkId:
    @pytest.mark.parametrize("shortened_link, expected_result",
                             [(f"{dev_domain}A1B2c3", "A1B2c3")])
    def test_get_shortened_link_id(self, shortened_link,  expected_result):
        assert get_shortened_link_id(shortened_link=shortened_link) == expected_result
