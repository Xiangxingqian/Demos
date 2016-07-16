rem Cobertura命令行使用步骤：
rem 第一步： 插桩字节码 cobertura-instrument.bat [--basedir dir] [--datafile file] [--auxClasspath classPath] [--destination dir] [--ignore regex] classes [...]
rem 第二步： 运行程序 java -cp C:\cobertura\lib\cobertura.jar;C:\MyProject\build\instrumented;C:\MyProject\build\classes;C:\MyProject\build\test-classes -Dnet.sourceforge.cobertura.datafile=C:\MyProject\build\cobertura.ser ASimpleTestCase
rem 第三步： 生成测试结果 cobertura-report.bat [--datafile file] [--destination dir] [--format (html|xml)] [--encoding encoding] source code directory [...] [--basedir dir file underneath basedir ...]

rem Demo

cobertura-instrument.bat --destination E:\workspace\HelloWorld\instrumented E:\workspace\HelloWorld\classes
java -cp .\lib\cobertura.jar;.\lib\slf4j-api-1.7.5.jar;\E:\workspace\HelloWorld\instrumented;E:\workspace\HelloWorld\classes;E:\workspace\HelloWorld\test-classes -Dnet.sourceforge.cobertura.datafile=E:\workspace\HelloWorld\cobertura.ser Main
cobertura-report.bat --format xml --datafile E:\workspace\HelloWorld\cobertura.ser --destination E:\workspace\HelloWorld\reports\coverage E:\workspace\HelloWorld\src