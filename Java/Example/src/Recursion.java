
public class Recursion {
	public static void main(String argsp[]){
		print();
	}
	
	public static void print(){
		boolean isRunning = true;
		System.out.println("Hello");
		if(isRunning == true){
			print();
		}
	}
}
