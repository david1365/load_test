//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by Fernflower decompiler)
//

package ir.navaco.mcb.grinder;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FilenameFilter;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.OpenOption;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Map.Entry;

public class Main {
    public static String filePath = "D:\\NEWCONF\\GrinderAnalyzer.V2.b19\\logs";
    public static Path destFile = Paths.get("D:\\NEWCONF\\GrinderAnalyzer.V2.b19\\destFile.log");
    static final String pointStr = "Final statistics for this process";
    static final String pointTotalStr = "Totals ";
    static boolean reachPoint = false;
    static boolean reachPointTotal = false;
    static Map<String, TestResult> testResultMap = new HashMap();

    public Main() {
    }

    public static void main(String[] args) throws IOException {
        if (args.length >= 2 && args.length <= 2) {
            filePath = args[0];
            destFile = Paths.get(args[1]);
        } else {
            System.out.println("Usage : java -jar grinderMerge.jar {logPath} {destination merged log file}");
        }

        File dir = new File(filePath);
        File[] files = dir.listFiles(new FilenameFilter() {
            public boolean accept(File dir, String name) {
                return name.endsWith(".log") && !name.endsWith("data.log");
            }
        });
        List<String> lines = new ArrayList();
        lines.add("2018-08-11 15:41:02,090 INFO  mcb-n1-clone-38 : The Grinder version 3.11\n2018-08-11 15:41:02,093 INFO  mcb-n1-clone-38 : Java(TM) SE Runtime Environment 1.8.0_171-b11: Java HotSpot(TM) 64-Bit Server VM (25.171-b11, mixed mode) on Linux amd64 3.10.0-693.el7.x86_64\n2018-08-11 15:41:02,098 INFO  mcb-n1-clone-38 : time zone is IRDT (+0430)\n2018-08-11 15:41:02,196 INFO  mcb-n1-clone-38 : worker process 38 of agent number 0\n2018-08-11 15:41:02,260 INFO  mcb-n1-clone-38 : instrumentation agents: byte code transforming instrumenter for Jython 2.5; byte code transforming instrumenter for Java\n2018-08-11 15:41:06,434 INFO  mcb-n1-clone-38 : registered plug-in net.grinder.plugin.http.HTTPPlugin\n2018-08-11 15:41:14,510 INFO  mcb-n1-clone-38 : running \"main.py\" using Jython 2.5.3 (2.5:c56500f08d34+, Aug 13 2012, 14:54:35) \n[Java HotSpot(TM) 64-Bit Server VM (Oracle Corporation)]\n2018-08-11 15:43:06,981 INFO  mcb-n1-clone-38 : Final statistics for this process:\n2018-08-11 15:43:07,004 INFO  mcb-n1-clone-38 : \n             Tests        Errors       Mean Test    Test Time    TPS          Mean         Response     Response     Mean time to Mean time to Mean time to \n                                       Time (ms)    Standard                  response     bytes per    errors       resolve host establish    first byte   \n                                                    Deviation                 length       second                                 connection                \n                                                    (ms)                                                                                                    \n");
        File[] var4 = files;
        int var5 = files.length;

        for(int var6 = 0; var6 < var5; ++var6) {
            File filename = var4[var6];

            try {
                Scanner scanner = new Scanner(filename);
                Throwable var9 = null;

                try {
                    scanner.useDelimiter("[\\n]");

                    label217:
                    while(true) {
                        do {
                            while(true) {
                                String token;
                                do {
                                    if (!scanner.hasNext()) {
                                        break label217;
                                    }

                                    token = scanner.next();
                                } while(token.length() <= 0);

                                if (!reachPoint) {
                                    reachPoint = token.contains("Final statistics for this process");
                                    break;
                                }

                                if (!reachPointTotal) {
                                    if (token.contains("Totals ")) {
                                        break label217;
                                    }

                                    TestResult testResult = ParseToken(token);
                                    if (!testResultMap.containsKey(testResult.getTestNumber())) {
                                        testResultMap.put(testResult.getTestNumber(), testResult);
                                    } else {
                                        testResultMap.put(testResult.getTestNumber(), MergeTestResults(testResult, (TestResult)testResultMap.get(testResult.getTestNumber())));
                                    }
                                }
                            }
                        } while(!reachPoint);

                        for(int i = 1; i <= 6; ++i) {
                            scanner.next();
                        }
                    }
                } catch (Throwable var20) {
                    var9 = var20;
                    throw var20;
                } finally {
                    if (scanner != null) {
                        if (var9 != null) {
                            try {
                                scanner.close();
                            } catch (Throwable var19) {
                                var9.addSuppressed(var19);
                            }
                        } else {
                            scanner.close();
                        }
                    }

                }
            } catch (FileNotFoundException var22) {
                var22.printStackTrace();
            }

            reachPoint = false;
            reachPointTotal = false;
        }

        TestResult total = new TestResult();
        total.setTestNumber("Totals");
        total.setTestName("");
        total.setMeanResponseLength(new Double(0.0D));
        total.setMeanTimeToEstablishConnection(new Double(0.0D));
        total.setMeanTimeToFirstByte(new Double(0.0D));
        total.setErrors(new Long(0L));
        total.setMeanTestTime(new Double(0.0D));
        total.setTests(new Long(0L));
        total.setTestTimeStandardDeviation(new Double(0.0D));
        total.setTps(new Double(0.0D));
        total.setResponseBytesPerSecound(new Double(0.0D));
        total.setResponseErrors(new Long(0L));
        total.setMeanTimeToResolveHost(new Double(0.0D));
        Iterator var24 = testResultMap.entrySet().iterator();

        while(var24.hasNext()) {
            Entry<String, TestResult> testResultEntry = (Entry)var24.next();
            lines.add(((TestResult)testResultEntry.getValue()).toString());
            total.setMeanResponseLength(total.getMeanResponseLength() + ((TestResult)testResultEntry.getValue()).getMeanResponseLength());
            total.setMeanTimeToEstablishConnection(total.getMeanTimeToEstablishConnection() + ((TestResult)testResultEntry.getValue()).getMeanTimeToEstablishConnection());
            total.setMeanTimeToFirstByte(total.getMeanTimeToFirstByte() + ((TestResult)testResultEntry.getValue()).getMeanTimeToFirstByte());
            total.setErrors(total.getErrors() + ((TestResult)testResultEntry.getValue()).getErrors());
            total.setMeanTestTime(total.getMeanTestTime() + ((TestResult)testResultEntry.getValue()).getMeanTestTime());
            total.setTests(total.getTests() + ((TestResult)testResultEntry.getValue()).getTests());
            total.setTestTimeStandardDeviation(total.getTestTimeStandardDeviation() + ((TestResult)testResultEntry.getValue()).getTestTimeStandardDeviation());
            total.setTps(total.getTps() + ((TestResult)testResultEntry.getValue()).getTps());
            total.setResponseBytesPerSecound(total.getResponseBytesPerSecound() + ((TestResult)testResultEntry.getValue()).getResponseBytesPerSecound());
            total.setResponseErrors(total.getResponseErrors() + ((TestResult)testResultEntry.getValue()).getResponseErrors());
            total.setMeanTimeToResolveHost(total.getMeanTimeToResolveHost() + ((TestResult)testResultEntry.getValue()).getMeanTimeToResolveHost());
        }

        total.setMeanResponseLength(total.getMeanResponseLength() / (double)testResultMap.entrySet().size());
        total.setMeanTimeToEstablishConnection(total.getMeanTimeToEstablishConnection() / (double)testResultMap.entrySet().size());
        total.setMeanTimeToFirstByte(total.getMeanTimeToFirstByte() / (double)testResultMap.entrySet().size());
        total.setMeanTestTime(total.getMeanTestTime() / (double)testResultMap.entrySet().size());
        total.setTestTimeStandardDeviation(total.getTestTimeStandardDeviation() / (double)testResultMap.entrySet().size());
        total.setMeanTimeToResolveHost(total.getMeanTimeToResolveHost() / (double)testResultMap.entrySet().size());
        lines.add("");
        lines.add(total.toString());
        StringBuilder stringBuilder = new StringBuilder();
        Iterator var27 = lines.iterator();

        while(var27.hasNext()) {
            String line = (String)var27.next();
            stringBuilder.append(line);
            stringBuilder.append("\n");
        }

        Files.write(destFile, stringBuilder.toString().getBytes(Charset.forName("UTF-8")), new OpenOption[0]);
    }

    private static TestResult MergeTestResults(TestResult testResultFirst, TestResult testResultSecond) {
        TestResult mergedTestResult = new TestResult();
        mergedTestResult.setTestNumber(testResultFirst.getTestNumber());
        mergedTestResult.setTests(testResultFirst.getTests() + testResultSecond.getTests());
        mergedTestResult.setErrors(testResultFirst.getErrors() + testResultSecond.getErrors());
        mergedTestResult.setMeanTestTime((testResultFirst.getMeanTestTime() + testResultSecond.getMeanTestTime()) / 2.0D);
        mergedTestResult.setTestTimeStandardDeviation((testResultFirst.getTestTimeStandardDeviation() + testResultSecond.getTestTimeStandardDeviation()) / 2.0D);
        mergedTestResult.setTps(testResultFirst.getTps() + testResultSecond.getTps());
        mergedTestResult.setMeanResponseLength((testResultFirst.getMeanResponseLength() + testResultSecond.getMeanResponseLength()) / 2.0D);
        mergedTestResult.setResponseBytesPerSecound((testResultFirst.getResponseBytesPerSecound() + testResultSecond.getResponseBytesPerSecound()) / 2.0D);
        mergedTestResult.setResponseErrors(testResultFirst.getResponseErrors() + testResultSecond.getResponseErrors());
        mergedTestResult.setMeanTimeToResolveHost((testResultFirst.getMeanTimeToResolveHost() + testResultSecond.getMeanTimeToResolveHost()) / 2.0D);
        mergedTestResult.setMeanTimeToEstablishConnection((testResultFirst.getMeanTimeToEstablishConnection() + testResultSecond.getMeanTimeToEstablishConnection()) / 2.0D);
        mergedTestResult.setMeanTimeToFirstByte((testResultFirst.getMeanTimeToFirstByte() + testResultSecond.getMeanTimeToFirstByte()) / 2.0D);
        mergedTestResult.setTestName(testResultFirst.getTestName());
        return mergedTestResult;
    }

    private static TestResult ParseToken(String token) {
        TestResult testResult = new TestResult();
        testResult.setTestNumber(token.substring(0, 12));
        testResult.setTests(Long.parseLong(token.substring(13, 25).trim()));
        testResult.setErrors(Long.parseLong(token.substring(26, 38).trim()));
        testResult.setMeanTestTime(Double.parseDouble(token.substring(39, 51).trim()));
        testResult.setTestTimeStandardDeviation(Double.parseDouble(token.substring(52, 64).trim()));
        testResult.setTps(Double.parseDouble(token.substring(65, 77).trim()));
        testResult.setMeanResponseLength(Double.parseDouble(token.substring(78, 90).trim()));
        testResult.setResponseBytesPerSecound(Double.parseDouble(token.substring(91, 103).trim()));
        testResult.setResponseErrors(Long.parseLong(token.substring(104, 116).trim()));
        testResult.setMeanTimeToResolveHost(Double.parseDouble(token.substring(117, 129).replace("-", "0").trim()));
        testResult.setMeanTimeToEstablishConnection(Double.parseDouble(token.substring(130, 142).replace("-", "0").trim()));
        testResult.setMeanTimeToFirstByte(Double.parseDouble(token.substring(143, 156).trim()));
        testResult.setTestName(token.substring(157).trim());
        return testResult;
    }
}
