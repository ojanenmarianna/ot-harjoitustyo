

import com.mycompany.unicafe.Kassapaate;
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
public class KassapaateTest {
    Kassapaate paate;
    Maksukortti kortti;
    
    public KassapaateTest() {
    }
    
    @BeforeClass
    public static void setUpClass() {
    }
    
    @AfterClass
    public static void tearDownClass() {
    }
    
    @Before
    public void setUp() {
        paate = new Kassapaate();
        kortti = new Maksukortti(500);
    }
    
    @After
    public void tearDown() {
    }

    @Test
    public void kassassaRahaaOikeaMaaraAlussa() {
        assertEquals(100000, paate.kassassaRahaa());
    }
    
    @Test
    public void myytyjenLounaidenMaaraAlussaOikein() {
        assertEquals(0 + " " + 0, + paate.edullisiaLounaitaMyyty() + " " + paate.maukkaitaLounaitaMyyty());
    }
    
     @Test
    public void syoEdullisestiKateisellaToimii() {
        assertEquals(20 + ", " + 1 + ", " + 100240, paate.syoEdullisesti(260), paate.edullisiaLounaitaMyyty(), paate.kassassaRahaa());
    }
    
    @Test
    public void syoEullisestiKunKateistaLiianVahan() {
        assertEquals(220, paate.syoEdullisesti(220));
    }
    
    @Test
    public void syoMaukkaastiKateisellaToimii() {
        assertEquals(100 + " " + 1 + " " + 100400, paate.syoMaukkaasti(500), paate.maukkaitaLounaitaMyyty(), paate.kassassaRahaa());
    }
    
    @Test
    public void syoMaukkaastiKunKateistaLiianVahan() {
        assertEquals(240 + ", " + 0 + ", " + 100000, paate.syoMaukkaasti(240), paate.maukkaitaLounaitaMyyty(), paate.kassassaRahaa());
    }
    
    @Test
    public void syoEdullisestiToimiiKortilla() {
        assertEquals(true + " " + 260 + " " + 1, paate.syoEdullisesti(kortti) + " " + kortti.saldo() + " " + paate.edullisiaLounaitaMyyty());
    }
    
    @Test
    public void syoEdullisestiKunKortinSaldoEiRiita() {
        paate.syoMaukkaasti(kortti);
        assertEquals(false + " " + 100 + " " + 0, paate.syoEdullisesti(kortti) + " " + kortti.saldo() + " " + paate.edullisiaLounaitaMyyty());
    }
    
    @Test 
    public void syoMaukkaastiKortillaToimii() {
        assertEquals(true + " " + 100 + " " + 1, paate.syoMaukkaasti(kortti) + " " + kortti.saldo() + " " + paate.maukkaitaLounaitaMyyty());
    }
    
    @Test
    public void syoMaukkaastiKunKortillaLiianVahanSaldoa() {
        paate.syoEdullisesti(kortti);
        assertEquals(false + " " + 260 + " " + 0, paate.syoMaukkaasti(kortti) + " " + kortti.saldo() + " " + paate.maukkaitaLounaitaMyyty());
    }
    
    @Test
    public void kassanRahamaaraSamaKortilla() {
        paate.syoEdullisesti(kortti);
        assertEquals(100000, paate.kassassaRahaa());
    }
    
    @Test
    public void kortilleRahanLatausToimii() {
        paate.lataaRahaaKortille(kortti, 500);
        assertEquals(1000 + " " + 100500, kortti.saldo() + " " + paate.kassassaRahaa());
    }
    
    @Test
    public void eiNegatiivisiaLatauksia() {
        paate.lataaRahaaKortille(kortti, -10);
        assertEquals(500 + " " + 100000, kortti.saldo() +" " + paate.kassassaRahaa());
    }
}
