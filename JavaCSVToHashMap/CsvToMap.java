package JavaCSVToHashMap;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class CsvToMap {
    private File csv;
    public CsvToMap(File f){
        csv = f;
    }
    public Map<String,ArrayList<String>> csvToMap() throws FileNotFoundException {
        Scanner reader = new Scanner(csv);
        Map<String, ArrayList<String>> map = new HashMap<String,ArrayList<String>>();
        ArrayList<String> key = new ArrayList<String>();
        key.add("name");
        int lvl = 0;
        while(reader.hasNext()){
            String str =reader.nextLine();
            String vtr = str;

            if(str.startsWith(",")){
                vtr = str.substring(1);
            }else{
                key.add(returnArrayList(vtr).get(0));
                lvl++;

            }
            if(vtr.startsWith("20")){
                String mtr =vtr.substring(vtr.indexOf(",")+1);
                vtr = "";
                vtr = mtr;
            }
            map.put(key.get(lvl),returnArrayList(vtr));

        }
        return map;
    }
    private ArrayList<String> returnArrayList(String vtr){
        String addString = "";

        ArrayList<String> line = new ArrayList<String>();
        for(int i = 0; i < vtr.length(); i++){
            if(vtr.charAt(i) != ','){
                addString = addString + vtr.charAt(i);
            }else{
                line.add(addString);
                addString = "";
            }

        }
        return line;
    }
    public String getStudentsAttendance(Map<String,ArrayList<String>> inputMap,String date,String student) {
        int studentNumber = inputMap.get("name").indexOf(student);
        try{
            if(studentNumber == -1){
                return "Student Not Found";
            }else{
                return inputMap.get(date).get(studentNumber);
            }

        }catch(Exception ignored){

        }
        return inputMap.get(date).get(studentNumber);
    }
}
