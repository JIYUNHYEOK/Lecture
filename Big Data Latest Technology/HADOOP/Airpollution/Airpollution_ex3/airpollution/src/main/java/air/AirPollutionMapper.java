package air;

import java.io.IOException;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class AirPollutionMapper extends Mapper<Object, Text, Text, Text>{
	
	Text station = new Text();
	Text values = new Text();
	@Override
	protected void map(Object key, Text value, Mapper<Object, Text, Text, Text>.Context context)
			throws IOException, InterruptedException {
		
		// load line split by ","
		String[] ap = (value.toString()).split(",");
		try {
			if (ap[2].equals(Integer.toString(1))) {
				// Measurement data + Situation code
				station = new Text((ap[0]).toString() + "_" + (ap[1]).toString());
				// Average Value : 1, 3, 5, 6, 8, 9 // so2, no2, co, o3, pm10, pm2.5
				values = new Text("1:" + ap[3]);
				
				// Measurement data + Situation code & average value : mapping
				context.write(station, values);
			}
			else if (ap[2].equals(Integer.toString(3))) {
				// Measurement data + Situation code
				station = new Text((ap[0]).toString() + "_" + (ap[1]).toString());
				// Average Value : 1, 3, 5, 6, 8, 9 // so2, no2, co, o3, pm10, pm2.5
				values = new Text("3:" + ap[3]);
				
				// Measurement data + Situation code & average value : mapping
				context.write(station, values);
			}
			else if (ap[2].equals(Integer.toString(5))) {
				// Measurement data + Situation code
				station = new Text((ap[0]).toString() + "_" + (ap[1]).toString());
				// Average Value : 1, 3, 5, 6, 8, 9 // so2, no2, co, o3, pm10, pm2.5
				values = new Text("5:" + ap[3]);
				
				// Measurement data + Situation code & average value : mapping
				context.write(station, values);
			}
			else if (ap[2].equals(Integer.toString(6))) {
				// Measurement data + Situation code
				station = new Text((ap[0]).toString() + "_" + (ap[1]).toString());
				// Average Value : 1, 3, 5, 6, 8, 9 // so2, no2, co, o3, pm10, pm2.5
				values = new Text("6:" + ap[3]);
				
				// Measurement data + Situation code & average value : mapping
				context.write(station, values);
			}
			else if (ap[2].equals(Integer.toString(8))) {
				// Measurement data + Situation code
				station = new Text((ap[0]).toString() + "_" + (ap[1]).toString());
				// Average Value : 1, 3, 5, 6, 8, 9 // so2, no2, co, o3, pm10, pm2.5
				values = new Text("8:" + ap[3]);
				
				// Measurement data + Situation code & average value : mapping
				context.write(station, values);
			}
			else if (ap[2].equals(Integer.toString(9))) {
				// Measurement data + Situation code
				station = new Text((ap[0]).toString() + "_" + (ap[1]).toString());
				// Average Value : 1, 3, 5, 6, 8, 9 // so2, no2, co, o3, pm10, pm2.5
				values = new Text("9:" + ap[3]);
				
				// Measurement data + Situation code & average value : mapping
				context.write(station, values);
			}
				
		}
		// first column row NumberFormatException ignore
		catch (NumberFormatException e) {
		}
		
		
	}

}


