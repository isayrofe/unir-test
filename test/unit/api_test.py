import http.client
import os
import unittest
from urllib.request import urlopen, HTTPError

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/2/0"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}: {e.reason}"
            )
        else:
            self.fail(f"Se esperaba un error 400, pero se recibió una respuesta exitosa: {response.status}")   
        

    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_power_by_zero(self):
        url = f"{BASE_URL}/calc/power/0/-1"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}: {e.reason}"
            )
        else:
            self.fail(f"Se esperaba un error 400, pero se recibía una respuesta exitosa: {response.status}")
    def test_api_square_root(self):
        url = f"{BASE_URL}/calc/square_root/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_square_root_by_negative(self):
        url = f"{BASE_URL}/calc/square_root/-2"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}: {e.reason}"
            )
        else:
            self.fail(f"Se esperaba un error 400, pero se recibía una respuesta exitosa: {response.status}")
        
    
    def test_api_square_root_by_negative_float(self):
        url = f"{BASE_URL}/calc/square_root/-2.5"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}: {e.reason}"
            )
        else:
            self.fail(f"Se esperaba un error 400, pero se recibía una respuesta exitosa: {response.status}")

    def test_logarithm_method_returns_correct_result(self):
        url = f"{BASE_URL}/calc/logarithm/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_logarithm_by_zero(self):
        url = f"{BASE_URL}/calc/logarithm/0"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}: {e.reason}"
            )
        else:
            self.fail(f"Se esperaba un error 400, pero se recibía una respuesta exitosa: {response.status}")
        