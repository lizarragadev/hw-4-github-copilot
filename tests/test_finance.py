import unittest
import sys
import os

# Agregar el directorio padre al path para importar finance
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from finance import calculate_compound_interest, calculate_annuity_payment, calculate_internal_rate_of_return


class TestFinanceFunctions(unittest.TestCase):
    
    def test_calculate_compound_interest_normal_case(self):
        """Prueba el cálculo de interés compuesto con valores normales"""
        result = calculate_compound_interest(1000, 0.05, 10)
        expected = 1628.8946267344056
        self.assertAlmostEqual(result, expected, places=2)
    
    def test_calculate_compound_interest_zero_rate(self):
        """Prueba con tasa de interés cero"""
        result = calculate_compound_interest(1000, 0, 10)
        self.assertEqual(result, 1000)
    
    def test_calculate_compound_interest_zero_periods(self):
        """Prueba con cero períodos"""
        result = calculate_compound_interest(1000, 0.05, 0)
        self.assertEqual(result, 1000)
    
    def test_calculate_compound_interest_negative_principal(self):
        """Prueba con principal negativo"""
        result = calculate_compound_interest(-1000, 0.05, 10)
        expected = -1628.8946267344056
        self.assertAlmostEqual(result, expected, places=2)
    
    def test_calculate_annuity_payment_normal_case(self):
        """Prueba el cálculo de pago de anualidad con valores normales"""
        result = calculate_annuity_payment(10000, 0.05, 10)
        expected = 1295.0457491469873
        self.assertAlmostEqual(result, expected, places=2)
    
    def test_calculate_annuity_payment_zero_rate(self):
        """Prueba el pago de anualidad con tasa cero"""
        result = calculate_annuity_payment(10000, 0, 10)
        self.assertEqual(result, 1000)
    
    def test_calculate_annuity_payment_one_period(self):
        """Prueba con un solo período"""
        result = calculate_annuity_payment(1000, 0.05, 1)
        self.assertAlmostEqual(result, 1050, places=5)
    
    def test_calculate_annuity_payment_high_rate(self):
        """Prueba con tasa alta"""
        result = calculate_annuity_payment(10000, 0.20, 5)
        expected = 3343.7970328961514
        self.assertAlmostEqual(result, expected, places=2)
    
    def test_calculate_internal_rate_of_return_normal_case(self):
        """Prueba TIR con flujos de caja normales"""
        cash_flows = [-1000, 300, 300, 300, 300, 300]
        result = calculate_internal_rate_of_return(cash_flows)
        expected = 0.1524  # Aproximadamente 15.24%
        self.assertAlmostEqual(result, expected, places=3)
    
    def test_calculate_internal_rate_of_return_simple_case(self):
        """Prueba TIR con caso simple"""
        cash_flows = [-100, 110]
        result = calculate_internal_rate_of_return(cash_flows)
        expected = 0.1  # 10%
        self.assertAlmostEqual(result, expected, places=2)
    
    def test_calculate_internal_rate_of_return_negative_flows(self):
        """Prueba TIR con flujos negativos después de la inversión inicial"""
        cash_flows = [-1000, 500, -200, 800]
        result = calculate_internal_rate_of_return(cash_flows)
        # Verificar que el resultado es un número válido
        self.assertIsInstance(result, float)
    
    def test_calculate_internal_rate_of_return_zero_flows(self):
        """Prueba TIR con algunos flujos en cero"""
        cash_flows = [-1000, 0, 500, 600]
        result = calculate_internal_rate_of_return(cash_flows)
        self.assertIsInstance(result, float)
    
    def test_calculate_internal_rate_of_return_custom_iterations(self):
        """Prueba TIR con número personalizado de iteraciones"""
        cash_flows = [-1000, 300, 300, 300, 300, 300]
        result = calculate_internal_rate_of_return(cash_flows, iterations=50)
        expected = 0.1524
        self.assertAlmostEqual(result, expected, places=3)
    
    def test_calculate_internal_rate_of_return_derivative_zero_case(self):
        """Prueba TIR con caso que puede generar derivada cero"""
        # Caso edge: flujos que pueden causar que la derivada sea cero
        cash_flows = [0, 0, 0]  # Todos los flujos son cero
        result = calculate_internal_rate_of_return(cash_flows)
        # Verificar que el resultado es un número válido
        self.assertIsInstance(result, float)
    
    def test_calculate_internal_rate_of_return_single_iteration(self):
        """Prueba TIR con una sola iteración"""
        cash_flows = [-100, 110]
        result = calculate_internal_rate_of_return(cash_flows, iterations=1)
        # Con una sola iteración, debería devolver algo cercano al guess inicial
        self.assertIsInstance(result, float)
    
    def test_function_signatures_and_docstrings(self):
        """Prueba que las funciones tengan firmas y documentación correctas"""
        # Probar que las funciones existen y son callable
        self.assertTrue(callable(calculate_compound_interest))
        self.assertTrue(callable(calculate_annuity_payment))
        self.assertTrue(callable(calculate_internal_rate_of_return))
        
        # Verificar que tienen docstrings
        self.assertIsNotNone(calculate_compound_interest.__doc__)
        self.assertIsNotNone(calculate_annuity_payment.__doc__)
        self.assertIsNotNone(calculate_internal_rate_of_return.__doc__)
    
    def test_edge_cases_and_extreme_values(self):
        """Prueba casos extremos y valores límite"""
        # Compound interest con valores muy pequeños
        result = calculate_compound_interest(0.01, 0.001, 1)
        self.assertAlmostEqual(result, 0.01001, places=5)
        
        # Annuity payment con períodos muy grandes
        result = calculate_annuity_payment(1000000, 0.01, 1000)
        self.assertIsInstance(result, float)
        self.assertGreater(result, 0)
        
        # TIR con flujos muy grandes
        cash_flows = [-1000000, 500000, 600000]
        result = calculate_internal_rate_of_return(cash_flows)
        self.assertIsInstance(result, float)


if __name__ == '__main__':
    import coverage
    import subprocess
    import sys
    
    def run_tests_with_coverage():
        """Ejecuta todas las pruebas y muestra el coverage detallado"""
        print("=== Ejecutando pruebas unitarias con Coverage ===")
        
        # Configurar coverage
        cov = coverage.Coverage(
            source=['../finance'],  # Apuntar al módulo finance
            omit=['*/tests/*', '*/test_*']  # Excluir archivos de prueba
        )
        cov.start()
        
        # Importar después de iniciar coverage
        try:
            from finance import calculate_compound_interest, calculate_annuity_payment, calculate_internal_rate_of_return
        except ImportError as e:
            print(f"Error importando finance.py: {e}")
            return False
        
        # Ejecutar las pruebas
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromTestCase(TestFinanceFunctions)
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        
        # Detener coverage y guardar
        cov.stop()
        cov.save()
        
        print("\n" + "="*50)
        print("REPORTE DE COVERAGE")
        print("="*50)
        
        # Reporte en consola
        cov.report(show_missing=True)
        
        # Generar reporte HTML
        try:
            html_dir = os.path.join(os.path.dirname(__file__), 'coverage_html')
            cov.html_report(directory=html_dir)
            print(f"\n📊 Reporte HTML generado en: {html_dir}/index.html")
        except Exception as e:
            print(f"No se pudo generar reporte HTML: {e}")
        
        # Mostrar resumen de pruebas
        print(f"\n{'='*50}")
        print("RESUMEN DE PRUEBAS")
        print("="*50)
        print(f"✅ Pruebas ejecutadas: {result.testsRun}")
        print(f"❌ Fallos: {len(result.failures)}")
        print(f"⚠️  Errores: {len(result.errors)}")
        
        if result.failures:
            print(f"\n🔴 FALLOS ({len(result.failures)}):")
            for i, (test, traceback) in enumerate(result.failures, 1):
                print(f"{i}. {test}")
                print(f"   {traceback.split('AssertionError:')[-1].strip()}")
        
        if result.errors:
            print(f"\n🟠 ERRORES ({len(result.errors)}):")
            for i, (test, traceback) in enumerate(result.errors, 1):
                print(f"{i}. {test}")
                print(f"   {traceback.split('Error:')[-1].strip()}")
        
        # Calcular porcentaje de éxito
        success_rate = (result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100
        print(f"\n📈 Tasa de éxito: {success_rate:.1f}%")
        
        return result.wasSuccessful()
    
    def run_tests_with_subprocess():
        """Ejecuta las pruebas usando coverage como comando externo"""
        print("=== Ejecutando con Coverage CLI ===")
        
        # Cambiar al directorio padre para incluir finance.py
        parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        test_file = os.path.abspath(__file__)
        
        try:
            # Ejecutar coverage run
            print("Ejecutando: coverage run --source=. --omit=tests/* test_finance.py")
            result = subprocess.run([
                sys.executable, '-m', 'coverage', 'run',
                '--source=.',
                '--omit=tests/*,test_*',
                test_file
            ], cwd=parent_dir, capture_output=True, text=True)
            
            print("STDOUT:", result.stdout)
            if result.stderr:
                print("STDERR:", result.stderr)
            
            # Mostrar reporte
            print("\n" + "="*50)
            print("REPORTE DE COVERAGE")
            print("="*50)
            
            report_result = subprocess.run([
                sys.executable, '-m', 'coverage', 'report', '--show-missing'
            ], cwd=parent_dir, capture_output=True, text=True)
            
            print(report_result.stdout)
            
            # Generar reporte HTML
            html_result = subprocess.run([
                sys.executable, '-m', 'coverage', 'html',
                '-d', 'tests/coverage_html'
            ], cwd=parent_dir, capture_output=True, text=True)
            
            if html_result.returncode == 0:
                html_path = os.path.join(parent_dir, 'tests', 'coverage_html', 'index.html')
                print(f"\n📊 Reporte HTML: {html_path}")
            
            return result.returncode == 0
            
        except FileNotFoundError:
            print("Coverage no está instalado. Instala con: pip install coverage")
            return False
        except Exception as e:
            print(f"Error ejecutando coverage: {e}")
            return False
    
    def run_simple_tests():
        """Ejecuta pruebas sin coverage"""
        print("=== Ejecutando pruebas sin Coverage ===")
        
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromTestCase(TestFinanceFunctions)
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        
        print(f"\n📊 Resultados: {result.testsRun} pruebas, {len(result.failures)} fallos, {len(result.errors)} errores")
        return result.wasSuccessful()
    
    # Script principal
    print("🧪 SISTEMA DE PRUEBAS FINANCIERAS")
    print("="*50)
    
    # Intentar ejecutar con coverage
    success = False
    try:
        # Primer intento: coverage como módulo
        success = run_tests_with_coverage()
    except ImportError:
        print("⚠️  Coverage no está disponible como módulo")
        try:
            # Segundo intento: coverage como comando CLI
            success = run_tests_with_subprocess()
        except Exception as e:
            print(f"⚠️  No se pudo ejecutar coverage CLI: {e}")
            # Tercer intento: pruebas simples
            success = run_simple_tests()
    except Exception as e:
        print(f"⚠️  Error con coverage: {e}")
        success = run_simple_tests()
    
    # Resultado final
    if success:
        print("\n🎉 ¡TODAS LAS PRUEBAS PASARON!")
        print("✅ El módulo finance.py está funcionando correctamente")
    else:
        print("\n❌ ALGUNAS PRUEBAS FALLARON")
        print("🔧 Revisa los errores y corrige el código")
        sys.exit(1)
