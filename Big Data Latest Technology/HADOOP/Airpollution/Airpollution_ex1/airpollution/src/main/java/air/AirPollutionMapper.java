package air;

import java.io.IOException;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class AirPollutionMapper extends Mapper<Object, Text, Text, DoubleWritable>{
	
	Text station = new Text();
	@Override
	protected void map(Object key, Text value, Mapper<Object, Text, Text, DoubleWritable>.Context context)
			throws IOException, InterruptedException {

		// load line split by ","
		String[] ap = (value.toString()).split(",");
			// Item code == pm10(8)
			if (ap[2].equals(Integer.toString(8))) {
				// Average code == pm10's value
				DoubleWritable pm = new DoubleWritable(Double.parseDouble(ap[3]));
				// Situation code
				station = new Text(ap[1]);
				// Situation code & pm10's value : mapping
				context.write(station, pm);
			}
		
	}

}



