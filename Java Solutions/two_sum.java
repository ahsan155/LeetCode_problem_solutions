import java.util.Arrays;

public class two_sum {

	public int[] twoSum(int[] nums, int target) {
        int arrayLength = nums.length;
        int counter = 0;
        int[] resultArray = new int[0]; 
        
        while(counter < arrayLength){
            int pickedNum = nums[counter];
            int pickedIndex = counter;
            int otherCounter = 0;
            while(otherCounter < arrayLength){
                
                if(pickedNum == nums[otherCounter]  && counter==otherCounter) {
					break;
				}
				
                
                int total = pickedNum + nums[otherCounter];
                if(total == target){
                    resultArray = new int[2];
                    resultArray[0] = pickedIndex;
                    resultArray[1] = otherCounter;
                    break;
                }
                otherCounter++;
            }
            
            if(resultArray.length == 2){
                break;
            }
            
            counter++;
        }
        
        
        return resultArray; 
    }
	
}
