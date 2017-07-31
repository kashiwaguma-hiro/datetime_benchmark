import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.concurrent.TimeUnit;

public class Sample {

  public static void main(String[] args){
    String time = "20170101123456";
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyyMMddHHmmss");
    long start = System.currentTimeMillis();
    for(int i =0;i<100000;i++){
        LocalDateTime.parse(time, formatter);
    }
    System.out.println(((System.currentTimeMillis() - start)/1000d) + "sec");
  }
}
