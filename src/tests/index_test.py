import unittest
from io import StringIO
import sys
from contextlib import contextmanager
from index import main

@contextmanager
def captured_output():
    """Context manager to capture stdout"""
    new_out = StringIO()
    old_out = sys.stdout
    try:
        sys.stdout = new_out
        yield sys.stdout
    finally:
        sys.stdout = old_out

class TestIndex(unittest.TestCase):
    def test_main_function_output(self):
        with captured_output() as output:
            main()
        
        printed_lines = output.getvalue().strip().split('\n')
        
        # Test initial creation output
        self.assertEqual(printed_lines[0], "Luonnin jälkeen:")
        self.assertEqual(printed_lines[1], "Mehuvarasto: saldo = 0, vielä tilaa 100.0")
        self.assertEqual(printed_lines[2], "Olutvarasto: saldo = 20.2, vielä tilaa 79.8")
        
        # Test getters output
        self.assertEqual(printed_lines[3], "Olut getterit:")
        self.assertEqual(printed_lines[4], "saldo = 20.2")
        self.assertEqual(printed_lines[5], "tilavuus = 100.0")
        self.assertEqual(printed_lines[6], "paljonko_mahtuu = 79.8")
        
        # Test mehu setters output
        self.assertEqual(printed_lines[7], "Mehu setterit:")
        self.assertEqual(printed_lines[8], "Lisätään 50.7")
        self.assertEqual(printed_lines[9], "Mehuvarasto: saldo = 50.7, vielä tilaa 49.3")
        self.assertEqual(printed_lines[10], "Otetaan 3.14")
        self.assertEqual(printed_lines[11], "Mehuvarasto: saldo = 47.56, vielä tilaa 52.44")
        
        # Test error situations
        self.assertEqual(printed_lines[12], "Virhetilanteita:")
        self.assertEqual(printed_lines[13], "Varasto(-100.0);")
        self.assertEqual(printed_lines[14], "saldo = -100.0, vielä tilaa 100.0")
        self.assertEqual(printed_lines[15], "Varasto(100.0, -50.7)")
        self.assertEqual(printed_lines[16], "saldo = 0.0, vielä tilaa 100.0")
        
        # Test overflow and underflow situations
        self.assertEqual(printed_lines[17], "Olutvarasto: saldo = 20.2, vielä tilaa 79.8")
        self.assertEqual(printed_lines[18], "olutta.lisaa_varastoon(1000.0)")
        self.assertEqual(printed_lines[19], "Olutvarasto: saldo = 100.0, vielä tilaa 0.0")
        
        self.assertEqual(printed_lines[20], "Mehuvarasto: saldo = 47.56, vielä tilaa 52.44")
        self.assertEqual(printed_lines[21], "mehua.lisaa_varastoon(-666.0)")
        self.assertEqual(printed_lines[22], "Mehuvarasto: saldo = 47.56, vielä tilaa 52.44")
        
        self.assertEqual(printed_lines[23], "Olutvarasto: saldo = 100.0, vielä tilaa 0.0")
        self.assertEqual(printed_lines[24], "olutta.ota_varastosta(1000.0)")
        self.assertEqual(printed_lines[25], "saatiin 100.0")
        self.assertEqual(printed_lines[26], "Olutvarasto: saldo = 0.0, vielä tilaa 100.0")
        
        self.assertEqual(printed_lines[27], "Mehuvarasto: saldo = 47.56, vielä tilaa 52.44")
        self.assertEqual(printed_lines[28], "mehua.otaVarastosta(-32.9)")
        self.assertEqual(printed_lines[29], "saatiin 0.0")
        self.assertEqual(printed_lines[30], "Mehuvarasto: saldo = 47.56, vielä tilaa 52.44")