package air;

import java.io.IOException;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import java.lang.Double;

public class AirPollutionMapper extends Mapper<Object, Text, Text, DoubleWritable>{
	
	Text word = new Text();
	DoubleWritable one = new DoubleWritable(1);
	@Override
	protected void map(Object key, Text value, Mapper<Object, Text, Text, DoubleWritable>.Context context)
			throws IOException, InterruptedException {
		
		// load line split by ","
		String[] ap = (value.toString()).split(",");
		try {
			// Item code == pm10(8) or pm2.5(9)
			double pm1 = 30;
			double pm2 = 15;
			Double pm_value = Double.parseDouble(ap[3]);
			if ((ap[2].equals(Integer.toString(8)) && pm_value.compareTo(pm1) <= 0) || (ap[2].equals(Integer.toString(9)) && pm_value.compareTo(pm2) <= 0)) {
				// Average code == pm10 or pm2.5's value
				DoubleWritable pm = new DoubleWritable(Double.parseDouble(ap[3]));
				// Situation code
				Text station = new Text(ap[1]);
				// Situation code & pm10 or pm2.5's value : mapping
				context.write(station, pm);
			}
		}
		// first column row NumberFormatException ignore
		catch (NumberFormatException e) {
			
		}
	}

}





