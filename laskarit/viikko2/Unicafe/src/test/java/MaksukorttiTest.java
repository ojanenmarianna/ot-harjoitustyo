

import com.mycompany.unicafe.Maksukortti;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author marianna
 */
public class MaksukorttiTest {
    Maksukortti kortti;
    
    public MaksukorttiTest() {
    }
    
    @BeforeClass
    public static void setUpClass() {        
    }
    
    @AfterClass
    public static void tearDownClass() {
    }
    
    @Before
    public void setUp() {
        kortti = new Maksukortti(1000);
    }
    
    @After
    public void tearDown() {
    }

    @Test
    public void saldoAlussaOikein() {
        System.out.println(kortti.toString());
        assertEquals("saldo: 10.0", kortti.toString());
    }
    
    @Test
    public void rahanLataaminenKasvattaaSaldoaOikein() {
        kortti.lataaRahaa(200);
        assertEquals("saldo: 12.0", kortti.toString());
    }
    
    @Test
    public void rahanOttaminenToimiiOikein() {
        assertEquals(true + " " + 500, kortti.otaRahaa(500) + " " + kortti.saldo());
    }
    
    @Test
    public void saldoEiMuutuJosRahatEiRiita() {
        assertEquals(false + "saldo: 10.0", kortti.otaRahaa(1100)+ kortti.toString());
    }
    
    
}
