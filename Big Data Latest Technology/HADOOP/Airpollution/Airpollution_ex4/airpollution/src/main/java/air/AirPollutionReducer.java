package air;
import java.io.IOException;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class AirPollutionReducer extends Reducer<Text, Text, Text, Text>{

	@Override
	protected void reduce(Text key, Iterable<Text> values,
			Reducer<Text, Text, Text, Text>.Context context) throws IOException, InterruptedException {
		
		double sum1 = 0;
		double sum2 = 0;
		double sum3 = 0;
		double sum4 = 0;
		double sum5 = 0;
		double sum6 = 0;
		double count = 0;
		
		for(Text v : values) {
			sum1 += Double.parseDouble(v.toString().split(" ")[0]);
			sum2 += Double.parseDouble(v.toString().split(" ")[1]);
			sum3 += Double.parseDouble(v.toString().split(" ")[2]);
			sum4 += Double.parseDouble(v.toString().split(" ")[3]);
			sum5 += Double.parseDouble(v.toString().split(" ")[4]);
			sum6 += Double.parseDouble(v.toString().split(" ")[5]);
			count += 1;
		}
		
		Text result = new Text("SO2: " + Double.toString(sum1/count) + ", " + 
				"NO2: " + Double.toString(sum2/count) + ", " + 
				"CO: " + Double.toString(sum3/count) + ", " + 
				"O3: " + Double.toString(sum4/count) + ", " + 
				"PM10: " + Double.toString(sum5/count) + ", " + 
				"PM2.5: " + Double.toString(sum6/count));

		context.write(key, result);
	}
}




