The examples folder contains an unstructured tutorial on using the library



mergebuffer(buffer1, buffer2, xpos)

1. take two input buffers


```OOOOOO
OOOOOOOOOOOO
OOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
      OOOOOOOOOOOOOOOOOOOOOOO
            OOOOOOOOOOOOOOOOO
                  OOOOOOOOOOO
                        OOOOO
!!!
!!!!!!
!!!!!!!!!
!!!!!!!!!!!!
!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!
   !!!!!!!!!!!!!!!!!!!!!!!!
      !!!!!!!!!!!!!!!!!!!!!!!!
         !!!!!!!!!!!!!!!!!!!!!!!!
            !!!!!!!!!!!!!!!!!!!!!!!!
               !!!!!!!!!!!!!!!!!!!!!!!!
                  !!!!!!!!!!!!!!!!!!!!!!!!
                     !!!!!!!!!!!!!!!!!!!!!!!
                        !!!!!!!!!!!!!!!!!!!!
                           !!!!!!!!!!!!!!!!!
                              !!!!!!!!!!!!!!
                                 !!!!!!!!!!!
                                    !!!!!!!!
                                       !!!!!
                                          !!
```
2. pad the buffers so they are equal in size using padBuffer(buffer,xpr,ypre,xpost,ypost)                                                  
                                                  
```                
          OOOOOO                                  
          OOOOOOOOOOOO                            
          OOOOOOOOOOOOOOOOOO                      
          OOOOOOOOOOOOOOOOOOOOOOOO                
          OOOOOOOOOOOOOOOOOOOOOOOOOOOOO           
          OOOOOOOOOOOOOOOOOOOOOOOOOOOOO           
          OOOOOOOOOOOOOOOOOOOOOOOOOOOOO           
          OOOOOOOOOOOOOOOOOOOOOOOOOOOOO           
          OOOOOOOOOOOOOOOOOOOOOOOOOOOOO           
                OOOOOOOOOOOOOOOOOOOOOOO           
                      OOOOOOOOOOOOOOOOO           
                            OOOOOOOOOOO           
                                  OOOOO           
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
                                                  
   !!!                                            
   !!!!!!                                         
   !!!!!!!!!                                      
   !!!!!!!!!!!!                                   
   !!!!!!!!!!!!!!!                                
   !!!!!!!!!!!!!!!!!!                             
   !!!!!!!!!!!!!!!!!!!!!                          
   !!!!!!!!!!!!!!!!!!!!!!!!                       
      !!!!!!!!!!!!!!!!!!!!!!!!                    
         !!!!!!!!!!!!!!!!!!!!!!!!                 
            !!!!!!!!!!!!!!!!!!!!!!!!              
               !!!!!!!!!!!!!!!!!!!!!!!!           
                  !!!!!!!!!!!!!!!!!!!!!!!!        
                     !!!!!!!!!!!!!!!!!!!!!!!!     
                        !!!!!!!!!!!!!!!!!!!!!!!   
                           !!!!!!!!!!!!!!!!!!!!   
                              !!!!!!!!!!!!!!!!!   
                                 !!!!!!!!!!!!!!   
                                    !!!!!!!!!!!   
                                       !!!!!!!!   
                                          !!!!!   
                                             !!   
                                             
```
                                                  
3. to finally merge them on Xpos, bringing the first buffer to the front, and the second to the back and vice versa from xpos on, use distinctive chars for each buffer.
```
                                                  
                                                  
                                                  
                                                  
   !!!                                            
   !!!!!! OOOOOO                                  
   !!!!!!!OOOOOOOOOOOO                            
   !!!!!!!OOOOOOOOOOOOOOOOOO                      
   !!!!!!!OOOOOOOOOOOOOOOOOOOOOOOO                
   !!!!!!!OOOOOOOOOO!OOOOOOOOOOOOOOOOOO           
   !!!!!!!OOOOOOOOOO!!!!OOOOOOOOOOOOOOO           
   !!!!!!!OOOOOOOOOO!!!!!!!OOOOOOOOOOOO           
      !!!!OOOOOOOOOO!!!!!!!!!!OOOOOOOOO           
         !OOOOOOOOOO!!!!!!!!!!!!!OOOOOO           
            !!!!OOOO!!!!!!!!!!!!!!!!OOO           
               !!!!!!!!!!!!!!!!!!!!!!!!           
                  !!!!!!!!!!!!!!!!!!!!!!!!        
                     !!!!!!!!!!!!!!!!!!!!!!!!     
                        !!!!!!!!!!!!!!!!!!!!!!!   
                           !!!!!!!!!!!!!!!!!!!!   
                              !!!!!!!!!!!!!!!!!   
                                 !!!!!!!!!!!!!!   
                                    !!!!!!!!!!!   
                                       !!!!!!!!   
                                          !!!!!   
                                             !!   
```