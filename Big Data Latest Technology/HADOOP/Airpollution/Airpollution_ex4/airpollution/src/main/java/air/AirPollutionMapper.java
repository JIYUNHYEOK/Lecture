package air;

import java.io.IOException;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class AirPollutionMapper extends Mapper<Object, Text, Text, Text>{
	
	@Override
	protected void map(Object key, Text value, Mapper<Object, Text, Text, Text>.Context context)
			throws IOException, InterruptedException {
		
		
		// load line split by ","
		String[] ap = (value.toString()).split("\t");
		Text time = new Text((value.toString()).substring(11,16));
		Text avgval = new Text(ap[1]);
		context.write(time, avgval);	
	}

}









