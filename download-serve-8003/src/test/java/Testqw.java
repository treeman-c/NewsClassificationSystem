import com.classify.download.DownloadApplication;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import java.io.*;
import java.net.URLDecoder;

@RunWith(SpringRunner.class)
@SpringBootTest(classes = DownloadApplication.class)
public class Testqw {

    @Test
    public void test () throws IOException {
        String path = Testqw.class.getResource("/downloadfile/newsclassify.rar").getPath();
        path = URLDecoder.decode(path,"utf-8");
        File file  = new File(path);
        System.out.println(file);
        BufferedInputStream bf = new BufferedInputStream(new FileInputStream(file));
        byte[] bt = new byte[bf.available()];
        System.out.println(bt);
        bf.read(bt);
        System.out.println(bf);
        bf.close();

    }
}
