package com.classification.demo.controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;
@CrossOrigin(value = {"http://localhost:8080"})  //跨域问题注解
@RestController
public class ChartController {
        @Autowired
        private RestTemplate restTemplate;

        @RequestMapping(value = "/get-ch-data", method = RequestMethod.GET)
        public String GetData() {
                String result = unicodeToUtf8(restTemplate.getForEntity("http://py-sidecar/python/get_ch_data", String.class).getBody());
//                System.out.println(result);
                return result;
        }

        @RequestMapping(value = "/train-model", method = RequestMethod.GET)
        public void TrainModel() {
                restTemplate.getForEntity("http://py-sidecar/python/train_model", String.class);
        }


        /* *
         * @date 2022/3/31 16:46
         * @param [theString] Unicode编码的字符串
         * @return java.lang.String  utf-8编码的字符串
         */
        public static String unicodeToUtf8(String theString) {
                char aChar;
                int len = theString.length();
                StringBuffer outBuffer = new StringBuffer(len);
                for (int x = 0; x < len;) {
                        aChar = theString.charAt(x++);
                        if (aChar == '\\') {
                                aChar = theString.charAt(x++);
                                if (aChar == 'u') {
                                        // Read the xxxx
                                        int value = 0;
                                        for (int i = 0; i < 4; i++) {
                                                aChar = theString.charAt(x++);
                                                switch (aChar) {
                                                        case '0':
                                                        case '1':
                                                        case '2':
                                                        case '3':
                                                        case '4':
                                                        case '5':
                                                        case '6':
                                                        case '7':
                                                        case '8':
                                                        case '9':
                                                                value = (value << 4) + aChar - '0';
                                                                break;
                                                        case 'a':
                                                        case 'b':
                                                        case 'c':
                                                        case 'd':
                                                        case 'e':
                                                        case 'f':
                                                                value = (value << 4) + 10 + aChar - 'a';
                                                                break;
                                                        case 'A':
                                                        case 'B':
                                                        case 'C':
                                                        case 'D':
                                                        case 'E':
                                                        case 'F':
                                                                value = (value << 4) + 10 + aChar - 'A';
                                                                break;
                                                        default:
                                                                throw new IllegalArgumentException(
                                                                        "Malformed   \\uxxxx   encoding.");
                                                }
                                        }
                                        outBuffer.append((char) value);
                                } else {
                                        if (aChar == 't')
                                                aChar = '\t';
                                        else if (aChar == 'r')
                                                aChar = '\r';
                                        else if (aChar == 'n')
                                                aChar = '\n';
                                        else if (aChar == 'f')
                                                aChar = '\f';
                                        outBuffer.append(aChar);
                                }
                        } else
                                outBuffer.append(aChar);
                }
                return outBuffer.toString();
        }
}
