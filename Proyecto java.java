import com.mpatric.mp3agic.*;
import com.mpatric.mp3agic.Mp3File;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;


public class lector_mp3 {
    public static void mp3_fun(String cancion) throws Exception{
        // Lee el MP#
        Mp3File mp3file = new Mp3File(cancion);
        System.out.println("Duración canción: " + mp3file.getLengthInSeconds() + " segundos");
        System.out.println("Bitrate: " + mp3file.getBitrate() + " kbps " + (mp3file.isVbr() ? "(VBR)" : "(CBR)"));
        System.out.println("Sample rate: " + mp3file.getSampleRate() + " Hz");
        System.out.println("Tiene ID3v1 tag?: " + (mp3file.hasId3v1Tag() ? "SI" : "NO"));
        System.out.println("Tiene ID3v2 tag?: " + (mp3file.hasId3v2Tag() ? "YES" : "NO"));
        // Nos importa si tiene etiqueta DI3V2
        if (mp3file.hasId3v2Tag()) {
            ID3v2 id3v2Tag = mp3file.getId3v2Tag();
            System.out.println("#Canción: " + id3v2Tag.getTrack());
            System.out.println("Artista: " + id3v2Tag.getArtist());
            System.out.println("Título: " + id3v2Tag.getTitle());
            System.out.println("�?lbum: " + id3v2Tag.getAlbum());

            byte[] albumImageData = id3v2Tag.getAlbumImage();
            // Si tiene carátula guara la caratula como una imágen JPG
            if (albumImageData != null) {
                System.out.println("Have album image data, length: " + albumImageData.length + " bytes");
                System.out.println("Album image mime type: " + id3v2Tag.getAlbumImageMimeType());

                BufferedImage img = ImageIO.read(new ByteArrayInputStream(albumImageData));
                File outputfile = new File("caratula.jpg");
                ImageIO.write(img, "png", outputfile);
            }else{ // Si no tiene carátula, le pone una nueva a la canción y la guarda como una nueva.
                BufferedImage bImage = ImageIO.read(new File("sin_imagen.jpg"));
                ByteArrayOutputStream bos = new ByteArrayOutputStream();
                ImageIO.write(bImage, "jpg", bos );
                byte [] data = bos.toByteArray();
                id3v2Tag.setAlbumImage(data, "image/jpg");
                mp3file.save("nueva_"+cancion+".mp3");
            }
        }
    }

    public static void main(String[] args) throws Exception{
        String cancion = "jajejijoju.mp3"; // El nombre de la canción
        mp3_fun(cancion); // Se llama a la función que detalla el MP3
    }
}
