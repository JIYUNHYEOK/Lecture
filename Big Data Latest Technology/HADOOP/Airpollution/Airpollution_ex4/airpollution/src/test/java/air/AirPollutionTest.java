package air;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.util.ToolRunner;

public class AirPollutionTest {
	public static void main(String[] args) throws Exception {
		
		Configuration conf = new Configuration();
		conf.setInt("mapreduce.job.reduces", 3);
		
		String[] input_args = {"src/test/resources/Measurement_info_input4.txt"};
		ToolRunner.run(conf, new AirPollution(), input_args);
	}
}
