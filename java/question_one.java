import java.util.*;
class New {

	public static void main(String[] args) {
		
		int [] array = {1,2,3,4};
		nw(array);
	}
	
	public static void nw(int[] array) {
		for (int i=1; i<array.length; i++) {
			array[i] += array[i-1];
		}
		System.out.println(Arrays.toString(array));
		
	}

}