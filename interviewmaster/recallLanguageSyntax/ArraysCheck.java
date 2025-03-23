//declaring array with elements

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collector;

public class ArraysCheck {

    

    public static void main(String[] args) {
        int[] nums = {100,200,300,400};
        
        Arrays.stream(nums).boxed().collect(Collector.toList());


    }
}







