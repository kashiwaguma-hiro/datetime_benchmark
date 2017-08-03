import java.time.LocalDateTime;
import java.time.Duration;
import java.time.format.DateTimeFormatter;
import java.util.concurrent.TimeUnit;

public class IncrTime {
  private static final DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyyMMdd-HH:mm:ss");

  public static void main(String[] args){
    double size = 100000000d;
    LocalDateTime dateFrom = LocalDateTime.parse("20170101-00:00:00", formatter);
    LocalDateTime dateTo = LocalDateTime.parse("20171231-23:59:59", formatter);
    Duration diff = Duration.between(dateFrom, dateTo);

    Double incrSec = Double.valueOf(diff.getSeconds() / size); //秒精度
    long incrNano = (long)(incrSec.doubleValue()*1000d); // nano精度

    long start = System.currentTimeMillis();
    for(int i =0; i<size; i++){
       dateFrom = dateFrom.plusNanos(incrNano);
    }
    System.out.println(((System.currentTimeMillis() - start)/1000d) + "sec");
  }
}
