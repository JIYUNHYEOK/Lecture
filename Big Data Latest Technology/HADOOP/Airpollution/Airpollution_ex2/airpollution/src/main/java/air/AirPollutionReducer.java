package air;

import java.io.IOException;
import org.apache.hadoop.io.DoubleWritable;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class AirPollutionReducer extends Reducer<Text, DoubleWritable, Text, IntWritable>{
	
	IntWritable oval = new IntWritable();

	@Override
	protected void reduce(Text key, Iterable<DoubleWritable> values,
			Reducer<Text, DoubleWritable, Text, IntWritable>.Context context) throws IOException, InterruptedException {
		
		int count = 0;
		
		for(DoubleWritable v : values) {
			count += 1;
		}

		oval.set(count);

		context.write(key, oval);

		
	}
}







