import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.io.File;
public class CsvToArrayList {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner reader = new Scanner(new File("fake_data.csv"));
        List<ArrayList<Object>> TwoDArrayList = new ArrayList<ArrayList<Object>>();
        while(reader.next() != ",");

    }
}
