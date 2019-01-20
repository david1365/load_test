//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by Fernflower decompiler)
//

package ir.navaco.mcb.grinder;

public class TestResult {
    private String testNumber;
    private Long tests;
    private Long errors;
    private Double meanTestTime;
    private Double testTimeStandardDeviation;
    private Double tps;
    private Double meanResponseLength;
    private Double responseBytesPerSecound;
    private Long responseErrors;
    private Double meanTimeToResolveHost;
    private Double meanTimeToEstablishConnection;
    private Double meanTimeToFirstByte;
    private String testName;

    public TestResult() {
    }

    public String getTestNumber() {
        return this.testNumber;
    }

    public void setTestNumber(String testNumber) {
        this.testNumber = testNumber;
    }

    public Long getTests() {
        return this.tests;
    }

    public void setTests(Long tests) {
        this.tests = tests;
    }

    public Long getErrors() {
        return this.errors;
    }

    public void setErrors(Long errors) {
        this.errors = errors;
    }

    public Double getMeanTestTime() {
        return this.meanTestTime;
    }

    public void setMeanTestTime(Double meanTestTime) {
        this.meanTestTime = meanTestTime;
    }

    public Double getTestTimeStandardDeviation() {
        return this.testTimeStandardDeviation;
    }

    public void setTestTimeStandardDeviation(Double testTimeStandardDeviation) {
        this.testTimeStandardDeviation = testTimeStandardDeviation;
    }

    public Double getTps() {
        return this.tps;
    }

    public void setTps(Double tps) {
        this.tps = tps;
    }

    public Double getMeanResponseLength() {
        return this.meanResponseLength;
    }

    public void setMeanResponseLength(Double meanResponseLength) {
        this.meanResponseLength = meanResponseLength;
    }

    public Double getResponseBytesPerSecound() {
        return this.responseBytesPerSecound;
    }

    public void setResponseBytesPerSecound(Double responseBytesPerSecound) {
        this.responseBytesPerSecound = responseBytesPerSecound;
    }

    public Long getResponseErrors() {
        return this.responseErrors;
    }

    public void setResponseErrors(Long responseErrors) {
        this.responseErrors = responseErrors;
    }

    public Double getMeanTimeToResolveHost() {
        return this.meanTimeToResolveHost;
    }

    public void setMeanTimeToResolveHost(Double meanTimeToResolveHost) {
        this.meanTimeToResolveHost = meanTimeToResolveHost;
    }

    public Double getMeanTimeToEstablishConnection() {
        return this.meanTimeToEstablishConnection;
    }

    public void setMeanTimeToEstablishConnection(Double meanTimeToEstablishConnection) {
        this.meanTimeToEstablishConnection = meanTimeToEstablishConnection;
    }

    public Double getMeanTimeToFirstByte() {
        return this.meanTimeToFirstByte;
    }

    public void setMeanTimeToFirstByte(Double meanTimeToFirstByte) {
        this.meanTimeToFirstByte = meanTimeToFirstByte;
    }

    public String getTestName() {
        return this.testName;
    }

    public void setTestName(String testName) {
        this.testName = testName;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(this.getTestNumber());

        while(sb.length() < 13) {
            sb.append(' ');
        }

        sb.append(String.format("%d", this.getTests()));

        while(sb.length() < 26) {
            sb.append(' ');
        }

        sb.append(String.format("%d", this.getErrors()));

        while(sb.length() < 39) {
            sb.append(' ');
        }

        sb.append(String.format("%.2f", this.getMeanTestTime()));

        while(sb.length() < 52) {
            sb.append(' ');
        }

        sb.append(String.format("%.2f", this.getTestTimeStandardDeviation()));

        while(sb.length() < 65) {
            sb.append(' ');
        }

        sb.append(String.format("%.2f", this.getTps()));

        while(sb.length() < 78) {
            sb.append(' ');
        }

        sb.append(String.format("%.2f", this.getMeanResponseLength()));

        while(sb.length() < 91) {
            sb.append(' ');
        }

        sb.append(String.format("%.2f", this.getResponseBytesPerSecound()));

        while(sb.length() < 104) {
            sb.append(' ');
        }

        sb.append(String.format("%d", this.getResponseErrors()));

        while(sb.length() < 117) {
            sb.append(' ');
        }

        sb.append(String.format("%.2f", this.getMeanTimeToResolveHost()));

        while(sb.length() < 130) {
            sb.append(' ');
        }

        sb.append(String.format("%.2f", this.getMeanTimeToEstablishConnection()));

        while(sb.length() < 143) {
            sb.append(' ');
        }

        sb.append(String.format("%.2f", this.getMeanTimeToFirstByte()));

        while(sb.length() < 157) {
            sb.append(' ');
        }

        sb.append(this.getTestName());
        return sb.toString();
    }
}
