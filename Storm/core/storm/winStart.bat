::For running storm program on windows from command prompt

::Packaging Jars
call mvn clean install

::Running Topology on Storm locally
call storm jar target/storm-0.0.1-SNAPSHOT-jar-with-dependencies.jar com.ilbdaicnl.storm.TwitterStreamTopology