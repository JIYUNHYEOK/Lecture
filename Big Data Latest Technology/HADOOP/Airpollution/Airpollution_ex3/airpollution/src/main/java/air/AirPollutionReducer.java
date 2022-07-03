package air;

import java.io.IOException;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class AirPollutionReducer extends Reducer<Text, Text, Text, Text>{
	@Override
	protected void reduce(Text key, Iterable<Text> values,
			Reducer<Text, Text, Text, Text>.Context context) throws IOException, InterruptedException {
		
		Text oval = new Text();
		String[] airall = new String[6];
		String airval = "";
		
		for(Text v : values) {
			if (v.toString().split(":")[0].equals(Integer.toString(1))) {
				airall[0] = v.toString().split(":")[1];
			}
			else if (v.toString().split(":")[0].equals(Integer.toString(3))) {
				airall[1] = v.toString().split(":")[1];
			}
			else if (v.toString().split(":")[0].equals(Integer.toString(5))) {
				airall[2] = v.toString().split(":")[1];
			}
			else if (v.toString().split(":")[0].equals(Integer.toString(6))) {
				airall[3] = v.toString().split(":")[1];
			}
			else if (v.toString().split(":")[0].equals(Integer.toString(8))) {
				airall[4] = v.toString().split(":")[1];
			}
			else if (v.toString().split(":")[0].equals(Integer.toString(9))) {
				airall[5] = v.toString().split(":")[1];
			}
		}
		for (int i=0; i<airall.length; i++) {
			airval += airall[i] + " ";
		}
		oval.set(airval);
		context.write(key, oval);	
	}
}



