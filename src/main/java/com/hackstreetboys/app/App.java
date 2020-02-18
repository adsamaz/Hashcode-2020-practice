package com.hackstreetboys.app;

import java.util.List;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;
import javafx.util.Pair;

public class App 
{
    public static void main( String[] args )
    {
    	Pair<Integer, List<Integer>> inp = readPizzaSize("a_example.in");
        System.out.printf("Target: %d \nPizzas: ", inp.getKey());
        for(int pizza : inp.getValue()) {
        	System.out.printf("%d ", pizza);
        }
        
    }
    
    public static Pair<Integer, List<Integer>> readPizzaSize(String filename) {
    	List<Integer> pizzas = new ArrayList<Integer>();
    	int target = 0;
    	try {
    	      File myObj = new File("input/"+ filename);
    	      Scanner myReader = new Scanner(myObj);
    	      String[] header = myReader.nextLine().split(" ");
    	      target = Integer.parseInt(header[0]);
    	  
    	      String data = myReader.nextLine();
    	      for (String i : data.split(" ")) {
    	        	pizzas.add(Integer.parseInt(i));
    	      }
    	      myReader.close();
    	    } catch (FileNotFoundException e) {
    	      System.out.println("An error occurred.");
    	      e.printStackTrace();
    	    }
    	return new Pair<Integer, List<Integer>>(target, pizzas);
    }
}
