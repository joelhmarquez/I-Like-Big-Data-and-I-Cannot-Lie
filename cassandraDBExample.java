import com.datastax.driver.core.Cluster;
import com.datastax.driver.core.Session;

public class cassandraDBExample {

   public static void main(String args[]){

      //Query
      String query = "select * from cycling.cyclist_category;";
                    
      //creating Cluster object
      Cluster cluster = Cluster.builder().addContactPoint("127.0.0.1").build();
    
      //Creating Session object
      Session session = cluster.connect();
     
      //Executing the query
      session.execute(query);
     
      //using the KeySpace
      System.out.println(session.execute(query)); 
   }
}
