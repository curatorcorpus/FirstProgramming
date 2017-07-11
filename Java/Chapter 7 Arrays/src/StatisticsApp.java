
public class StatisticsApp {
	/** data fields */
	private static double mean;
	private static double stDev;
	private static int[] list = {1,2,3,4,5,6,7,8,9,10,
						11,12,13,14,15,16,17,18,19,20,
						21,22,23,24,25,26,27,28,29,30,
						31,32,33,34,35,36,37,38,39,40,
						41,42,43,44,45,46,47,48,49,50};
	
	
	/** main method */
	public static void main(String args[]){
		System.out.println("Mean: " + getMean(list));
		System.out.println("Standard Deviation: " + getStDev(list));
	}
	
	/** returns mean in double value */
	public static double getMean(int[] intList){
		// local variable
		double total = 0;
		
		for(int num : intList){
			total += num;
		}
		mean = total/intList.length;
		return mean;
	}
	
	/** returns standard deviation in double value */
	public static double getStDev(int[] intList){
		// local variables
		double std = 0;
		
		for(int num : intList){
			std += Math.pow(num - mean, 2);
		}
		
		stDev = Math.sqrt((std/(intList.length - 1)));
		return stDev;
	}
}
