package JavaCSVToHashMap;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Map;

public class CsvTest {
    public static void main(String[] args) throws FileNotFoundException {
        CsvToMap tester = new CsvToMap(new File("fake_data.csv"));
        Map<String,ArrayList<String>> test = tester.csvToMap();
        System.out.println(test);
        System.out.println("Student:" + test.get("name").get(1) + " Attendance:" + test.get("2020/10/22-08:50").get(1));
        System.out.println(tester.getStudentsAttendance(test,"2020/10/22-08:50","Charlie Ray"));
    }
}
