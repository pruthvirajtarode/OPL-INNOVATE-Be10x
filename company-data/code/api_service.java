package com.oplinnovate.api;

public class ApiService {
    public void processRequest(String vendor, int status) {
        if (status == 200) {
            System.out.println("Success for " + vendor);
        } else {
            // Code Smell: Swallowing exception without logging
            try {
                throw new Exception("API Failed");
            } catch (Exception e) {
                // Do nothing
            }
        }
    }
}
