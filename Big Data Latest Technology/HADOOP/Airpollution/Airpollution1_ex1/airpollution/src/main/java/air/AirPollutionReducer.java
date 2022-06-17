package air;

import java.io.IOException;
import org.apache.hadoop.io.DoubleWritable;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class AirPollutionReducer extends Reducer<Text, DoubleWritable, Text, Text>{
	
	DoubleWritable oval_avg = new DoubleWritable();
	DoubleWritable oval_min = new DoubleWritable();
	DoubleWritable oval_max = new DoubleWritable();
	Text all = new Text();
	@Override
	protected void reduce(Text key, Iterable<DoubleWritable> values,
			Reducer<Text, DoubleWritable, Text, Text>.Context context) throws IOException, InterruptedException {
		
		double sum = 0;
		double count = 0;
		double max = Integer.MIN_VALUE;
		double min = Integer.MAX_VALUE;
		
		for(DoubleWritable v : values) {
			sum += v.get();
			count += 1;
			if (v.get() > max) {
				max = v.get();
			}
			if (v.get() < min) {
				min = v.get();
			}
		}
		
		Double avg = sum/count;
		
		oval_min.set(min);
		oval_max.set(max);
		oval_avg.set(avg);
		
		all.set("average: " + oval_avg.toString() + ", max: " + oval_max.toString() + ", min: " + oval_min.toString());
		
		context.write(key, all);
		
	}
}








